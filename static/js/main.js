document.addEventListener('DOMContentLoaded', function() {
    const checkBtns = document.querySelectorAll('.check-btn');
    const hintBtns = document.querySelectorAll('.hint-btn');
    const completeBtn = document.getElementById('complete-btn');
    const submitAnswerBtns = document.querySelectorAll('.submit-answer');
    const terminalInputs = document.querySelectorAll('.terminal-input');

    let commandHistories = {};

    if (CONTINUE_STEP_ID && IS_AUTHENTICATED) {
        const stepElement = document.getElementById('step-' + CONTINUE_STEP_ID);
        if (stepElement) {
            stepElement.scrollIntoView({ behavior: 'smooth', block: 'center' });
            stepElement.classList.add('highlight-step');
        }
    }

    terminalInputs.forEach(input => {
        const stepId = input.dataset.stepId;
        commandHistories[stepId] = [];

        input.addEventListener('keydown', function(e) {
            if (e.key === 'Enter') {
                const command = input.value.trim();
                if (command) {
                    commandHistories[stepId].push(command);
                    addTerminalLine(stepId, command);
                    input.value = '';
                    checkCommand(stepId);
                }
            }
        });

        input.focus();
    });

    checkBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const stepId = this.dataset.stepId;
            checkCommand(stepId);
        });
    });

    hintBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const stepId = this.dataset.stepId;
            requestHint(stepId);
        });
    });

    submitAnswerBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const questionId = this.dataset.questionId;
            const stepId = this.dataset.stepId;
            submitQuizAnswer(questionId, stepId);
        });
    });

    if (completeBtn && IS_AUTHENTICATED) {
        completeBtn.addEventListener('click', function() {
            const lessonId = this.dataset.lessonId;
            saveProgress(lessonId, true);
        });
    }

    if (IS_AUTHENTICATED) {
        const interactiveSections = document.querySelectorAll('.interactive-section, .quiz-section');
        if (interactiveSections.length > 0) {
            fetch('/api/streak', { method: 'POST' })
                .then(r => r.json())
                .then(data => {
                    if (data.message === 'Серия обновлена!' || data.xp_gained > 0) {
                        let msg = 'Ежедневный вход: +' + data.xp_gained + ' XP';
                        if (data.streak_days >= 7) {
                            msg += ' (Бонус серии!)';
                        }
                        showNotification(msg);
                    }
                });
        }
    }

    function addTerminalLine(stepId, command) {
        const terminalBody = document.getElementById('terminal-body-' + stepId);
        const line = document.createElement('div');
        line.className = 'terminal-line';
        line.innerHTML = '<span class="prompt">user@gitlearn:~$</span><span class="command">' + escapeHtml(command) + '</span>';
        terminalBody.appendChild(line);
        terminalBody.scrollTop = terminalBody.scrollHeight;
    }

    function addTerminalOutput(stepId, output, isError) {
        const terminalBody = document.getElementById('terminal-body-' + stepId);
        const line = document.createElement('div');
        line.className = 'terminal-line';
        line.innerHTML = '<span class="output" style="color: ' + (isError ? '#ff4444' : '#a0a0a0') + '">' + output + '</span>';
        terminalBody.appendChild(line);
        terminalBody.scrollTop = terminalBody.scrollHeight;
    }

    function checkCommand(stepId) {
        const history = commandHistories[stepId];
        if (!history || history.length === 0) {
            showFeedback(stepId, 'Введите команду в терминал', false);
            return;
        }

        const lastCommand = history[history.length - 1];
        const interactiveSection = document.querySelector('.interactive-section[data-step-id="' + stepId + '"]');
        if (!interactiveSection) return;

        const expected = interactiveSection.dataset.expected;
        const lessonId = interactiveSection.dataset.lessonId;

        if (!expected) {
            showFeedback(stepId, 'Задание выполнено!', true);
            addTerminalOutput(stepId, '✓ Задание выполнено!', false);
            saveProgress(lessonId, true, stepId);
            return;
        }

        fetch('/api/verify-command', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                command: lastCommand,
                expected: expected,
                lesson_id: parseInt(lessonId),
                step_id: parseInt(stepId)
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.correct) {
                showFeedback(stepId, data.message, true);
                addTerminalOutput(stepId, '✓ ' + data.message, false);
                addTerminalOutput(stepId, '+' + data.points + ' опыта', false);
                
                if (data.lesson_completed) {
                    addTerminalOutput(stepId, '🎉 Урок пройден!', false);
                    showNotification('Урок пройден!');
                    if (completeBtn) {
                        completeBtn.textContent = 'Пройдено ✓';
                        completeBtn.disabled = true;
                    }
                }
                
                saveProgress(lessonId, data.lesson_completed, stepId);
            } else {
                showFeedback(stepId, data.message, false);
                addTerminalOutput(stepId, '✗ ' + data.message, true);
            }
        })
        .catch(error => {
            showFeedback(stepId, 'Ошибка при проверке команды', false);
        });
    }

    function requestHint(stepId) {
        const interactiveSection = document.querySelector('.interactive-section[data-step-id="' + stepId + '"]');
        if (!interactiveSection) return;

        const lessonId = interactiveSection.dataset.lessonId;
        const stepOrder = interactiveSection.dataset.stepOrder;
        const hintBtn = interactiveSection.querySelector('.hint-btn');
        
        fetch('/api/hint/' + lessonId + '/' + stepOrder, { method: 'POST' })
            .then(response => {
                if (!response.ok) {
                    return response.json().then(data => { throw new Error(data.error); });
                }
                return response.json();
            })
            .then(data => {
                if (data.content) {
                    const hintsContainer = document.getElementById('hints-' + stepId);
                    const hintEl = document.createElement('div');
                    hintEl.className = 'hint-display';
                    hintEl.innerHTML = '<strong>Подсказка:</strong> ' + data.content;
                    hintsContainer.appendChild(hintEl);
                    hintBtn.disabled = true;
                }
            })
            .catch(error => {
                showFeedback(stepId, error.message || 'Подсказка недоступна', false);
            });
    }

    function submitQuizAnswer(questionId, stepId) {
        const questionEl = document.querySelector('.quiz-question[data-question-id="' + questionId + '"]');
        const selectedInput = questionEl.querySelector('input[name="question-' + questionId + '"]:checked');
        
        if (!selectedInput) {
            showQuizFeedback(questionId, 'Выберите вариант ответа', false);
            return;
        }

        const answerId = selectedInput.value;
        const lessonId = questionEl.closest('.quiz-section').dataset.lessonId;

        fetch('/api/quiz/submit', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                question_id: parseInt(questionId),
                answer_id: parseInt(answerId),
                lesson_id: parseInt(lessonId),
                step_id: parseInt(stepId)
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.correct) {
                showQuizFeedback(questionId, 'Верно! +' + data.points + ' опыта', true);
                if (data.lesson_completed) {
                    showNotification('Урок пройден!');
                    if (completeBtn) {
                        completeBtn.textContent = 'Пройдено ✓';
                        completeBtn.disabled = true;
                    }
                }
            } else {
                showQuizFeedback(questionId, 'Неверно', false);
            }
        })
        .catch(error => {
            showQuizFeedback(questionId, 'Ошибка при отправке ответа', false);
        });
    }

    function showFeedback(stepId, message, isSuccess) {
        const feedback = document.getElementById('feedback-' + stepId);
        if (!feedback) return;

        feedback.textContent = message;
        feedback.className = 'feedback show ' + (isSuccess ? 'success' : 'error');

        setTimeout(() => {
            feedback.classList.remove('show');
        }, 5000);
    }

    function showQuizFeedback(questionId, message, isSuccess) {
        const feedback = document.getElementById('quiz-feedback-' + questionId);
        if (!feedback) return;

        feedback.textContent = message;
        feedback.className = 'feedback show ' + (isSuccess ? 'success' : 'error');

        setTimeout(() => {
            feedback.classList.remove('show');
        }, 5000);
    }

    function saveProgress(lessonId, completed, stepId) {
        if (!IS_AUTHENTICATED) return;

        fetch('/api/progress', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                lesson_id: parseInt(lessonId),
                completed: completed,
                current_step_id: stepId || null
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                if (completeBtn) {
                    completeBtn.textContent = 'Пройдено ✓';
                    completeBtn.disabled = true;
                }
            }
        })
        .catch(error => {
        });
    }

    function showNotification(message) {
        const notification = document.createElement('div');
        notification.className = 'notification';
        notification.textContent = message;
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.classList.add('show');
        }, 100);

        setTimeout(() => {
            notification.classList.remove('show');
            setTimeout(() => notification.remove(), 300);
        }, 3000);
    }

    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        const inputs = form.querySelectorAll('input');
        inputs.forEach(input => {
            input.addEventListener('keypress', function(e) {
                if (e.key === 'Enter' && input.type !== 'textarea') {
                    const submitBtn = form.querySelector('input[type="submit"], button[type="submit"]');
                    if (submitBtn) {
                        submitBtn.click();
                    }
                }
            });
        });
    });
});
