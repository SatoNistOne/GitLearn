document.addEventListener('DOMContentLoaded', function() {
    const terminalInput = document.getElementById('terminal-input');
    const terminalBody = document.getElementById('terminal-body');
    const checkBtn = document.getElementById('check-btn');
    const feedback = document.getElementById('feedback');
    const completeBtn = document.getElementById('complete-btn');
    const interactiveSection = document.querySelector('.interactive-section');

    let commandHistory = [];
    let historyIndex = -1;

    if (terminalInput) {
        terminalInput.addEventListener('keydown', function(e) {
            if (e.key === 'Enter') {
                const command = terminalInput.value.trim();
                if (command) {
                    commandHistory.push(command);
                    historyIndex = commandHistory.length;
                    addTerminalLine(command);
                    terminalInput.value = '';
                }
            } else if (e.key === 'ArrowUp') {
                e.preventDefault();
                if (historyIndex > 0) {
                    historyIndex--;
                    terminalInput.value = commandHistory[historyIndex];
                }
            } else if (e.key === 'ArrowDown') {
                e.preventDefault();
                if (historyIndex < commandHistory.length - 1) {
                    historyIndex++;
                    terminalInput.value = commandHistory[historyIndex];
                } else {
                    historyIndex = commandHistory.length;
                    terminalInput.value = '';
                }
            }
        });

        terminalInput.focus();
    }

    if (checkBtn && interactiveSection) {
        checkBtn.addEventListener('click', checkCommand);
    }

    if (completeBtn && IS_AUTHENTICATED) {
        completeBtn.addEventListener('click', function() {
            const lessonId = this.getAttribute('data-lesson-id');
            saveProgress(lessonId, true, 1);
        });
    }

    if (IS_AUTHENTICATED && !interactiveSection && completeBtn) {
        const lessonId = completeBtn.getAttribute('data-lesson-id');
        if (lessonId) {
            saveProgress(lessonId, true, 1);
        }
    }

    const nextLessonBtn = document.querySelector('.lesson-nav .btn-secondary[href*="lesson"]');
    if (nextLessonBtn && IS_AUTHENTICATED && interactiveSection) {
        nextLessonBtn.addEventListener('click', function(e) {
            const lessonId = interactiveSection.getAttribute('data-lesson-id');
            if (lessonId) {
                saveProgress(lessonId, true, 1);
            }
        });
    }

    function addTerminalLine(command) {
        const line = document.createElement('div');
        line.className = 'terminal-line';
        line.innerHTML = `<span class="prompt">user@gitlearn:~$</span><span class="command">${escapeHtml(command)}</span>`;
        terminalBody.appendChild(line);
        terminalBody.scrollTop = terminalBody.scrollHeight;
    }

    function addOutputLine(output, isError = false) {
        const line = document.createElement('div');
        line.className = 'terminal-line';
        line.innerHTML = `<span class="output" style="color: ${isError ? '#ff4444' : '#a0a0a0'}">${output}</span>`;
        terminalBody.appendChild(line);
        terminalBody.scrollTop = terminalBody.scrollHeight;
    }

    function checkCommand() {
        if (!terminalInput) return;

        const lastCommand = commandHistory[commandHistory.length - 1];
        if (!lastCommand) {
            showFeedback('Введите команду в терминал', false);
            return;
        }

        const expected = interactiveSection.getAttribute('data-expected');
        const lessonId = interactiveSection.getAttribute('data-lesson-id');

        if (!expected) {
            showFeedback('Задание не требует проверки команды. Просто выполните команду в терминале.', true);
            saveProgress(lessonId, true, 1);
            return;
        }

        fetch('/api/verify-command', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                command: lastCommand,
                expected: expected
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.correct) {
                showFeedback(data.message, true);
                addOutputLine('✓ ' + data.message, false);
            } else {
                showFeedback(data.message, false);
                addOutputLine('✗ ' + data.message, true);
            }
            saveProgress(lessonId, true, 1);
        })
        .catch(error => {
            showFeedback('Ошибка при проверке команды', false);
        });
    }

    function showFeedback(message, isSuccess) {
        if (!feedback) return;

        feedback.textContent = message;
        feedback.className = 'feedback show ' + (isSuccess ? 'success' : 'error');

        setTimeout(() => {
            feedback.classList.remove('show');
        }, 5000);
    }

    function saveProgress(lessonId, completed, currentStep) {
        if (!IS_AUTHENTICATED) return;

        fetch('/api/progress', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                lesson_id: parseInt(lessonId),
                completed: completed,
                current_step: currentStep
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
