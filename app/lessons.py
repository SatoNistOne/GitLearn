LESSONS_DATA = [
    {
        'title': 'Введение в Git',
        'slug': 'introduction',
        'order': 1,
        'description': 'Основы системы контроля версий Git',
        'difficulty': 'beginner',
        'estimated_time': 15,
        'steps': [
            {
                'title': 'Что такое Git?',
                'content': 'Git — это распределённая система контроля версий. Она позволяет отслеживать изменения в коде, возвращаться к предыдущим версиям и работать в команде.',
                'step_type': 'theory',
                'order': 1,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Основные понятия',
                'content': '''
<strong>Репозиторий</strong> — хранилище вашего проекта<br>
<strong>Коммит</strong> — сохранение изменений<br>
<strong>Ветка</strong> — независимая линия разработки
''',
                'step_type': 'theory',
                'order': 2,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Проверка знаний',
                'content': 'Ответьте на вопрос для закрепления материала',
                'step_type': 'quiz',
                'order': 3,
                'is_interactive': True,
                'points': 10
            }
        ],
        'hints': [],
        'quiz_questions': [
            {
                'question_text': 'Что такое Git?',
                'question_type': 'multiple_choice',
                'points': 10,
                'order': 1,
                'answers': [
                    {'answer_text': 'Система контроля версий', 'is_correct': True, 'order': 1},
                    {'answer_text': 'Язык программирования', 'is_correct': False, 'order': 2},
                    {'answer_text': 'Редактор кода', 'is_correct': False, 'order': 3},
                    {'answer_text': 'База данных', 'is_correct': False, 'order': 4}
                ]
            }
        ],
        'assets': [
            {'asset_type': 'cheatsheet', 'title': 'Шпаргалка по Git', 'content': 'Git — система контроля версий', 'order': 1}
        ]
    },
    {
        'title': 'Инициализация репозитория',
        'slug': 'init',
        'order': 2,
        'description': 'Создание нового Git репозитория',
        'difficulty': 'beginner',
        'estimated_time': 10,
        'steps': [
            {
                'title': 'Команда git init',
                'content': 'Первая команда, с которой начинается работа с Git — <code>git init</code>. Она создаёт новый репозиторий в текущей папке.',
                'step_type': 'theory',
                'order': 1,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Пример использования',
                'content': '''
<pre><code>git init</code></pre>
<p>После выполнения команды создаётся скрытая папка <code>.git</code>.</p>
''',
                'step_type': 'example',
                'order': 2,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Практическое задание',
                'content': 'Инициализируйте репозиторий в текущей директории',
                'step_type': 'practice',
                'order': 3,
                'is_interactive': True,
                'expected_command': 'git init',
                'points': 10
            }
        ],
        'hints': [
            {'step_id': 3, 'content': 'Команда состоит из двух слов: git и init', 'hint_order': 1, 'penalty_points': 5},
            {'step_id': 3, 'content': 'Введите: git init', 'hint_order': 2, 'penalty_points': 10}
        ],
        'quiz_questions': [
            {
                'question_text': 'Какая команда создаёт новый Git репозиторий?',
                'question_type': 'multiple_choice',
                'points': 10,
                'order': 1,
                'answers': [
                    {'answer_text': 'git start', 'is_correct': False, 'order': 1},
                    {'answer_text': 'git init', 'is_correct': True, 'order': 2},
                    {'answer_text': 'git create', 'is_correct': False, 'order': 3},
                    {'answer_text': 'git new', 'is_correct': False, 'order': 4}
                ]
            }
        ],
        'assets': []
    },
    {
        'title': 'Добавление файлов',
        'slug': 'add',
        'order': 3,
        'description': 'Добавление файлов в индекс Git',
        'difficulty': 'beginner',
        'estimated_time': 15,
        'steps': [
            {
                'title': 'Команда git add',
                'content': 'Команда <code>git add</code> добавляет файлы в область индексации (staging area) перед коммитом.',
                'step_type': 'theory',
                'order': 1,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Варианты использования',
                'content': '''
<pre><code>
git add filename.txt    # Добавить конкретный файл
git add .               # Добавить все файлы
git add *.py            # Добавить файлы по маске
</code></pre>
''',
                'step_type': 'example',
                'order': 2,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Практическое задание',
                'content': 'Добавьте файл main.py в индекс',
                'step_type': 'practice',
                'order': 3,
                'is_interactive': True,
                'expected_command': 'git add main.py',
                'points': 10
            }
        ],
        'hints': [
            {'step_id': 3, 'content': 'Используйте команду git add', 'hint_order': 1, 'penalty_points': 5},
            {'step_id': 3, 'content': 'Укажите имя файла после команды: git add main.py', 'hint_order': 2, 'penalty_points': 10}
        ],
        'quiz_questions': [
            {
                'question_text': 'Что делает команда git add?',
                'question_type': 'multiple_choice',
                'points': 10,
                'order': 1,
                'answers': [
                    {'answer_text': 'Создаёт новый файл', 'is_correct': False, 'order': 1},
                    {'answer_text': 'Добавляет файл в индекс', 'is_correct': True, 'order': 2},
                    {'answer_text': 'Удаляет файл', 'is_correct': False, 'order': 3},
                    {'answer_text': 'Копирует файл', 'is_correct': False, 'order': 4}
                ]
            }
        ],
        'assets': []
    },
    {
        'title': 'Создание коммита',
        'slug': 'commit',
        'order': 4,
        'description': 'Сохранение изменений в истории Git',
        'difficulty': 'beginner',
        'estimated_time': 15,
        'steps': [
            {
                'title': 'Команда git commit',
                'content': 'Команда <code>git commit</code> сохраняет изменения из индекса в историю репозитория.',
                'step_type': 'theory',
                'order': 1,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Формат команды',
                'content': '''
<pre><code>
git commit -m "Описание изменений"
git commit -am "Описание"
</code></pre>
''',
                'step_type': 'example',
                'order': 2,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Практическое задание',
                'content': 'Создайте коммит с сообщением "Initial commit"',
                'step_type': 'practice',
                'order': 3,
                'is_interactive': True,
                'expected_command': 'git commit -m "Initial commit"',
                'points': 10
            }
        ],
        'hints': [
            {'step_id': 3, 'content': 'Используйте флаг -m для сообщения', 'hint_order': 1, 'penalty_points': 5},
            {'step_id': 3, 'content': 'git commit -m "Initial commit"', 'hint_order': 2, 'penalty_points': 10}
        ],
        'quiz_questions': [
            {
                'question_text': 'Какой флаг используется для сообщения коммита?',
                'question_type': 'multiple_choice',
                'points': 10,
                'order': 1,
                'answers': [
                    {'answer_text': '-s', 'is_correct': False, 'order': 1},
                    {'answer_text': '-m', 'is_correct': True, 'order': 2},
                    {'answer_text': '-c', 'is_correct': False, 'order': 3},
                    {'answer_text': '-t', 'is_correct': False, 'order': 4}
                ]
            }
        ],
        'assets': []
    },
    {
        'title': 'Просмотр статуса',
        'slug': 'status',
        'order': 5,
        'description': 'Проверка состояния репозитория',
        'difficulty': 'beginner',
        'estimated_time': 10,
        'steps': [
            {
                'title': 'Команда git status',
                'content': 'Команда <code>git status</code> показывает текущее состояние репозитория.',
                'step_type': 'theory',
                'order': 1,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Практическое задание',
                'content': 'Проверьте статус репозитория',
                'step_type': 'practice',
                'order': 2,
                'is_interactive': True,
                'expected_command': 'git status',
                'points': 10
            }
        ],
        'hints': [
            {'step_id': 2, 'content': 'Команда состоит из двух слов', 'hint_order': 1, 'penalty_points': 5}
        ],
        'quiz_questions': [],
        'assets': []
    },
    {
        'title': 'Просмотр истории',
        'slug': 'log',
        'order': 6,
        'description': 'Просмотр истории коммитов',
        'difficulty': 'beginner',
        'estimated_time': 15,
        'steps': [
            {
                'title': 'Команда git log',
                'content': 'Команда <code>git log</code> показывает историю коммитов.',
                'step_type': 'theory',
                'order': 1,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Опции команды',
                'content': '''
<pre><code>
git log              # Полная история
git log --oneline    # Краткий формат
git log -5           # Последние 5 коммитов
</code></pre>
''',
                'step_type': 'example',
                'order': 2,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Практическое задание',
                'content': 'Просмотрите историю коммитов в кратком формате',
                'step_type': 'practice',
                'order': 3,
                'is_interactive': True,
                'expected_command': 'git log --oneline',
                'points': 10
            }
        ],
        'hints': [
            {'step_id': 3, 'content': 'Используйте git log с флагом', 'hint_order': 1, 'penalty_points': 5},
            {'step_id': 3, 'content': 'git log --oneline', 'hint_order': 2, 'penalty_points': 10}
        ],
        'quiz_questions': [],
        'assets': []
    },
    {
        'title': 'Работа с ветками',
        'slug': 'branch',
        'order': 7,
        'description': 'Создание и управление ветками',
        'difficulty': 'intermediate',
        'estimated_time': 20,
        'steps': [
            {
                'title': 'Команда git branch',
                'content': 'Ветки позволяют вести независимую разработку.',
                'step_type': 'theory',
                'order': 1,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Основные команды',
                'content': '''
<pre><code>
git branch              # Показать все ветки
git branch feature      # Создать ветку
git branch -d feature   # Удалить ветку
</code></pre>
''',
                'step_type': 'example',
                'order': 2,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Практическое задание',
                'content': 'Создайте новую ветку с именем feature',
                'step_type': 'practice',
                'order': 3,
                'is_interactive': True,
                'expected_command': 'git branch feature',
                'points': 10
            }
        ],
        'hints': [
            {'step_id': 3, 'content': 'Используйте команду git branch с именем ветки', 'hint_order': 1, 'penalty_points': 5},
            {'step_id': 3, 'content': 'git branch feature', 'hint_order': 2, 'penalty_points': 10}
        ],
        'quiz_questions': [],
        'assets': []
    },
    {
        'title': 'Переключение между ветками',
        'slug': 'checkout',
        'order': 8,
        'description': 'Переключение между ветками Git',
        'difficulty': 'intermediate',
        'estimated_time': 15,
        'steps': [
            {
                'title': 'Команда git checkout',
                'content': 'Команда <code>git checkout</code> переключает между ветками.',
                'step_type': 'theory',
                'order': 1,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Практическое задание',
                'content': 'Переключитесь на ветку main',
                'step_type': 'practice',
                'order': 2,
                'is_interactive': True,
                'expected_command': 'git checkout main',
                'points': 10
            }
        ],
        'hints': [
            {'step_id': 2, 'content': 'Используйте команду git checkout', 'hint_order': 1, 'penalty_points': 5},
            {'step_id': 2, 'content': 'git checkout main', 'hint_order': 2, 'penalty_points': 10}
        ],
        'quiz_questions': [],
        'assets': []
    },
    {
        'title': 'Слияние веток',
        'slug': 'merge',
        'order': 9,
        'description': 'Объединение изменений из разных веток',
        'difficulty': 'intermediate',
        'estimated_time': 20,
        'steps': [
            {
                'title': 'Команда git merge',
                'content': 'Команда <code>git merge</code> объединяет изменения из одной ветки в другую.',
                'step_type': 'theory',
                'order': 1,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Практическое задание',
                'content': 'Слейте ветку feature в текущую ветку',
                'step_type': 'practice',
                'order': 2,
                'is_interactive': True,
                'expected_command': 'git merge feature',
                'points': 10
            }
        ],
        'hints': [
            {'step_id': 2, 'content': 'Используйте команду git merge', 'hint_order': 1, 'penalty_points': 5},
            {'step_id': 2, 'content': 'git merge feature', 'hint_order': 2, 'penalty_points': 10}
        ],
        'quiz_questions': [],
        'assets': []
    },
    {
        'title': 'Отмена изменений',
        'slug': 'revert-reset',
        'order': 10,
        'description': 'Отмена изменений в Git',
        'difficulty': 'intermediate',
        'estimated_time': 20,
        'steps': [
            {
                'title': 'git revert и git reset',
                'content': 'Для отмены изменений используются команды <code>git revert</code> и <code>git reset</code>.',
                'step_type': 'theory',
                'order': 1,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Разница между командами',
                'content': '''
<pre><code>
git revert HEAD      # Отменить коммит (безопасно)
git reset --soft HEAD~1   # Отменить коммит
git reset --hard HEAD~1   # Полностью отменить
</code></pre>
''',
                'step_type': 'example',
                'order': 2,
                'is_interactive': False,
                'points': 0
            }
        ],
        'hints': [],
        'quiz_questions': [],
        'assets': []
    },
    {
        'title': 'Удалённые репозитории',
        'slug': 'remote',
        'order': 11,
        'description': 'Работа с удалёнными репозиториями',
        'difficulty': 'intermediate',
        'estimated_time': 15,
        'steps': [
            {
                'title': 'Команда git remote',
                'content': 'Команда <code>git remote</code> управляет удалёнными репозиториями.',
                'step_type': 'theory',
                'order': 1,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Практическое задание',
                'content': 'Добавьте удалённый репозиторий с именем origin',
                'step_type': 'practice',
                'order': 2,
                'is_interactive': True,
                'expected_command': 'git remote add origin https://github.com/user/repo.git',
                'points': 10
            }
        ],
        'hints': [
            {'step_id': 2, 'content': 'Используйте команду git remote add', 'hint_order': 1, 'penalty_points': 5},
            {'step_id': 2, 'content': 'git remote add origin https://github.com/user/repo.git', 'hint_order': 2, 'penalty_points': 10}
        ],
        'quiz_questions': [],
        'assets': []
    },
    {
        'title': 'Отправка изменений',
        'slug': 'push',
        'order': 12,
        'description': 'Отправка изменений в удалённый репозиторий',
        'difficulty': 'intermediate',
        'estimated_time': 15,
        'steps': [
            {
                'title': 'Команда git push',
                'content': 'Команда <code>git push</code> отправляет ваши коммиты в удалённый репозиторий.',
                'step_type': 'theory',
                'order': 1,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Практическое задание',
                'content': 'Отправьте изменения в удалённый репозиторий',
                'step_type': 'practice',
                'order': 2,
                'is_interactive': True,
                'expected_command': 'git push origin main',
                'points': 10
            }
        ],
        'hints': [
            {'step_id': 2, 'content': 'Используйте команду git push', 'hint_order': 1, 'penalty_points': 5},
            {'step_id': 2, 'content': 'git push origin main', 'hint_order': 2, 'penalty_points': 10}
        ],
        'quiz_questions': [],
        'assets': []
    },
    {
        'title': 'Получение изменений',
        'slug': 'pull-fetch',
        'order': 13,
        'description': 'Получение изменений из удалённого репозитория',
        'difficulty': 'intermediate',
        'estimated_time': 15,
        'steps': [
            {
                'title': 'git pull и git fetch',
                'content': 'Команды для получения изменений из удалённого репозитория.',
                'step_type': 'theory',
                'order': 1,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Практическое задание',
                'content': 'Получите и объедините изменения из удалённого репозитория',
                'step_type': 'practice',
                'order': 2,
                'is_interactive': True,
                'expected_command': 'git pull origin main',
                'points': 10
            }
        ],
        'hints': [
            {'step_id': 2, 'content': 'Используйте команду git pull', 'hint_order': 1, 'penalty_points': 5},
            {'step_id': 2, 'content': 'git pull origin main', 'hint_order': 2, 'penalty_points': 10}
        ],
        'quiz_questions': [],
        'assets': []
    },
    {
        'title': 'Игнорирование файлов',
        'slug': 'gitignore',
        'order': 14,
        'description': 'Настройка .gitignore для исключения файлов',
        'difficulty': 'beginner',
        'estimated_time': 10,
        'steps': [
            {
                'title': 'Файл .gitignore',
                'content': 'Файл <code>.gitignore</code> указывает Git, какие файлы не нужно отслеживать.',
                'step_type': 'theory',
                'order': 1,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Пример .gitignore',
                'content': '''
<pre><code>
*.log
node_modules/
.env
__pycache__/
</code></pre>
''',
                'step_type': 'example',
                'order': 2,
                'is_interactive': False,
                'points': 0
            }
        ],
        'hints': [],
        'quiz_questions': [],
        'assets': []
    },
    {
        'title': 'Конфликты слияния',
        'slug': 'conflicts',
        'order': 15,
        'description': 'Разрешение конфликтов при слиянии',
        'difficulty': 'advanced',
        'estimated_time': 25,
        'steps': [
            {
                'title': 'Что такое конфликт',
                'content': 'Конфликты возникают, когда одна и та же строка изменена в разных ветках.',
                'step_type': 'theory',
                'order': 1,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Как выглядит конфликт',
                'content': '''
<pre><code>
<<<<<<< HEAD
old_value = 10
=======
old_value = 20
>>>>>>> feature
</code></pre>
''',
                'step_type': 'example',
                'order': 2,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Шаги разрешения',
                'content': '''
<ol>
    <li>Откройте файл с конфликтом</li>
    <li>Выберите нужную версию кода</li>
    <li>Удалите маркеры конфликта</li>
    <li>Сохраните файл</li>
    <li>git add file.txt</li>
    <li>git commit</li>
</ol>
''',
                'step_type': 'theory',
                'order': 3,
                'is_interactive': False,
                'points': 0
            }
        ],
        'hints': [],
        'quiz_questions': [],
        'assets': []
    },
    {
        'title': 'Временное сохранение изменений',
        'slug': 'stash',
        'order': 16,
        'description': 'Сохранение незакоммиченных изменений для последующего возвращения',
        'difficulty': 'intermediate',
        'estimated_time': 15,
        'steps': [
            {
                'title': 'Команда git stash',
                'content': 'Команда <code>git stash</code> временно сохраняет незакоммиченные изменения и очищает рабочую директорию.',
                'step_type': 'theory',
                'order': 1,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Пример использования',
                'content': '''
<pre><code>
git stash                    # Сохранить изменения
git stash list               # Показать список stash
git stash pop                # Применить и удалить stash
git stash apply              # Применить stash без удаления
</code></pre>
''',
                'step_type': 'example',
                'order': 2,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Практическое задание',
                'content': 'Сохраните изменения во временное хранилище',
                'step_type': 'practice',
                'order': 3,
                'is_interactive': True,
                'expected_command': 'git stash',
                'points': 10
            }
        ],
        'hints': [
            {'step_id': 3, 'content': 'Используйте команду git stash', 'hint_order': 1, 'penalty_points': 5}
        ],
        'quiz_questions': [],
        'assets': []
    },
    {
        'title': 'Просмотр различий',
        'slug': 'diff',
        'order': 17,
        'description': 'Сравнение изменений между коммитами и файлами',
        'difficulty': 'beginner',
        'estimated_time': 15,
        'steps': [
            {
                'title': 'Команда git diff',
                'content': 'Команда <code>git diff</code> показывает различия между файлами в рабочей директории и индексом.',
                'step_type': 'theory',
                'order': 1,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Варианты использования',
                'content': '''
<pre><code>
git diff                     # Все изменения
git diff file.txt            # Изменения в файле
git diff --staged            # Изменения в индексе
git diff commit1 commit2     # Между коммитами
</code></pre>
''',
                'step_type': 'example',
                'order': 2,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Практическое задание',
                'content': 'Просмотрите все изменения в репозитории',
                'step_type': 'practice',
                'order': 3,
                'is_interactive': True,
                'expected_command': 'git diff',
                'points': 10
            }
        ],
        'hints': [
            {'step_id': 3, 'content': 'Используйте команду git diff', 'hint_order': 1, 'penalty_points': 5}
        ],
        'quiz_questions': [],
        'assets': []
    },
    {
        'title': 'Удаление файлов',
        'slug': 'rm',
        'order': 18,
        'description': 'Удаление файлов из репозитория и рабочей директории',
        'difficulty': 'beginner',
        'estimated_time': 10,
        'steps': [
            {
                'title': 'Команда git rm',
                'content': 'Команда <code>git rm</code> удаляет файлы из репозитория и рабочей директории.',
                'step_type': 'theory',
                'order': 1,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Пример использования',
                'content': '''
<pre><code>
git rm file.txt              # Удалить файл
git rm -r folder/            # Удалить директорию
git rm --cached file.txt     # Удалить только из индекса
</code></pre>
''',
                'step_type': 'example',
                'order': 2,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Практическое задание',
                'content': 'Удалите файл old.txt из репозитория',
                'step_type': 'practice',
                'order': 3,
                'is_interactive': True,
                'expected_command': 'git rm old.txt',
                'points': 10
            }
        ],
        'hints': [
            {'step_id': 3, 'content': 'Используйте команду git rm', 'hint_order': 1, 'penalty_points': 5}
        ],
        'quiz_questions': [],
        'assets': []
    },
    {
        'title': 'Переименование файлов',
        'slug': 'mv',
        'order': 19,
        'description': 'Перемещение и переименование файлов в Git',
        'difficulty': 'beginner',
        'estimated_time': 10,
        'steps': [
            {
                'title': 'Команда git mv',
                'content': 'Команда <code>git mv</code> перемещает или переименовывает файлы.',
                'step_type': 'theory',
                'order': 1,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Пример использования',
                'content': '''
<pre><code>
git mv old.txt new.txt       # Переименовать файл
git mv file.txt folder/      # Переместить в директорию
</code></pre>
''',
                'step_type': 'example',
                'order': 2,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Практическое задание',
                'content': 'Переименуйте файл main.py в app.py',
                'step_type': 'practice',
                'order': 3,
                'is_interactive': True,
                'expected_command': 'git mv main.py app.py',
                'points': 10
            }
        ],
        'hints': [
            {'step_id': 3, 'content': 'Используйте команду git mv', 'hint_order': 1, 'penalty_points': 5}
        ],
        'quiz_questions': [],
        'assets': []
    },
    {
        'title': 'Просмотр коммитов',
        'slug': 'show',
        'order': 20,
        'description': 'Детальный просмотр информации о коммите',
        'difficulty': 'intermediate',
        'estimated_time': 15,
        'steps': [
            {
                'title': 'Команда git show',
                'content': 'Команда <code>git show</code> показывает информацию о коммите и изменения в нём.',
                'step_type': 'theory',
                'order': 1,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Пример использования',
                'content': '''
<pre><code>
git show                     # Последний коммит
git show commit-hash         # Конкретный коммит
git show --stat              # Со статистикой
</code></pre>
''',
                'step_type': 'example',
                'order': 2,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Практическое задание',
                'content': 'Просмотрите информацию о последнем коммите',
                'step_type': 'practice',
                'order': 3,
                'is_interactive': True,
                'expected_command': 'git show',
                'points': 10
            }
        ],
        'hints': [
            {'step_id': 3, 'content': 'Используйте команду git show', 'hint_order': 1, 'penalty_points': 5}
        ],
        'quiz_questions': [],
        'assets': []
    },
    {
        'title': 'Отмена коммита',
        'slug': 'reset-commit',
        'order': 21,
        'description': 'Отмена последнего коммита с сохранением изменений',
        'difficulty': 'intermediate',
        'estimated_time': 15,
        'steps': [
            {
                'title': 'Отмена коммита',
                'content': 'Для отмены последнего коммита используйте <code>git reset HEAD~1</code>. Изменения останутся в рабочей директории.',
                'step_type': 'theory',
                'order': 1,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Пример использования',
                'content': '''
<pre><code>
git reset HEAD~1             # Отменить коммит
git reset --hard HEAD~1      # Отменить коммит и изменения
</code></pre>
''',
                'step_type': 'example',
                'order': 2,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Практическое задание',
                'content': 'Отмените последний коммит',
                'step_type': 'practice',
                'order': 3,
                'is_interactive': True,
                'expected_command': 'git reset HEAD~1',
                'points': 10
            }
        ],
        'hints': [
            {'step_id': 3, 'content': 'Используйте git reset HEAD~1', 'hint_order': 1, 'penalty_points': 5}
        ],
        'quiz_questions': [],
        'assets': []
    },
    {
        'title': 'Работа с тегами',
        'slug': 'tag',
        'order': 22,
        'description': 'Создание и управление тегами для версий',
        'difficulty': 'intermediate',
        'estimated_time': 15,
        'steps': [
            {
                'title': 'Команда git tag',
                'content': 'Теги используются для маркировки конкретных версий проекта.',
                'step_type': 'theory',
                'order': 1,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Пример использования',
                'content': '''
<pre><code>
git tag                      # Показать все теги
git tag v1.0                 # Создать тег
git tag -a v1.0 -m "Release" # Аннотированный тег
git push origin v1.0         # Отправить тег
</code></pre>
''',
                'step_type': 'example',
                'order': 2,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Практическое задание',
                'content': 'Создайте тег с именем v1.0',
                'step_type': 'practice',
                'order': 3,
                'is_interactive': True,
                'expected_command': 'git tag v1.0',
                'points': 10
            }
        ],
        'hints': [
            {'step_id': 3, 'content': 'Используйте команду git tag', 'hint_order': 1, 'penalty_points': 5}
        ],
        'quiz_questions': [],
        'assets': []
    },
    {
        'title': 'Клонирование репозитория',
        'slug': 'clone',
        'order': 23,
        'description': 'Создание локальной копии удалённого репозитория',
        'difficulty': 'beginner',
        'estimated_time': 10,
        'steps': [
            {
                'title': 'Команда git clone',
                'content': 'Команда <code>git clone</code> создаёт локальную копию удалённого репозитория.',
                'step_type': 'theory',
                'order': 1,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Пример использования',
                'content': '''
<pre><code>
git clone url                  # Клонировать репозиторий
git clone url folder-name      # Клонировать в папку
git clone --depth 1 url        # Клонировать без истории
</code></pre>
''',
                'step_type': 'example',
                'order': 2,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Практическое задание',
                'content': 'Склонируйте репозиторий с GitHub',
                'step_type': 'practice',
                'order': 3,
                'is_interactive': True,
                'expected_command': 'git clone https://github.com/user/repo.git',
                'points': 10
            }
        ],
        'hints': [
            {'step_id': 3, 'content': 'Используйте команду git clone', 'hint_order': 1, 'penalty_points': 5}
        ],
        'quiz_questions': [],
        'assets': []
    },
    {
        'title': 'Обновление репозитория',
        'slug': 'fetch',
        'order': 24,
        'description': 'Получение изменений из удалённого репозитория без слияния',
        'difficulty': 'intermediate',
        'estimated_time': 15,
        'steps': [
            {
                'title': 'Команда git fetch',
                'content': 'Команда <code>git fetch</code> загружает изменения из удалённого репозитория, но не объединяет их.',
                'step_type': 'theory',
                'order': 1,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Пример использования',
                'content': '''
<pre><code>
git fetch origin             # Получить изменения
git fetch --all              # Получить все удалённые репозитории
git fetch origin branch      # Получить конкретную ветку
</code></pre>
''',
                'step_type': 'example',
                'order': 2,
                'is_interactive': False,
                'points': 0
            },
            {
                'title': 'Практическое задание',
                'content': 'Получите изменения из удалённого репозитория',
                'step_type': 'practice',
                'order': 3,
                'is_interactive': True,
                'expected_command': 'git fetch origin',
                'points': 10
            }
        ],
        'hints': [
            {'step_id': 3, 'content': 'Используйте команду git fetch', 'hint_order': 1, 'penalty_points': 5}
        ],
        'quiz_questions': [],
        'assets': []
    }
]
