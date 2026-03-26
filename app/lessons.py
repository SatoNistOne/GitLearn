LESSONS_DATA = [
    {
        'title': 'Введение в Git',
        'slug': 'introduction',
        'order': 1,
        'content': '''
<h2>Что такое Git?</h2>
<p>Git — это распределённая система контроля версий. Она позволяет отслеживать изменения в коде, возвращаться к предыдущим версиям и работать в команде.</p>

<h3>Основные понятия:</h3>
<ul>
    <li><strong>Репозиторий</strong> — хранилище вашего проекта</li>
    <li><strong>Коммит</strong> — сохранение изменений</li>
    <li><strong>Ветка</strong> — независимая линия разработки</li>
</ul>

<h3>Зачем нужен Git?</h3>
<p>Git помогает:</p>
<ul>
    <li>Хранить историю изменений</li>
    <li>Работать в команде без конфликтов</li>
    <li>Экспериментировать с кодом безопасно</li>
</ul>
''',
        'interactive_task': None,
        'expected_output': None
    },
    {
        'title': 'Инициализация репозитория',
        'slug': 'init',
        'order': 2,
        'content': '''
<h2>git init</h2>
<p>Первая команда, с которой начинается работа с Git — <code>git init</code>. Она создаёт новый репозиторий в текущей папке.</p>

<h3>Как использовать:</h3>
<pre><code>git init</code></pre>

<p>После выполнения команды создаётся скрытая папка <code>.git</code>, где хранится вся информация о версиях.</p>

<h3>Пример:</h3>
<pre><code>
$ mkdir my-project
$ cd my-project
$ git init
Initialized empty Git repository in my-project/.git/
</code></pre>
''',
        'interactive_task': 'Инициализируйте репозиторий в текущей директории',
        'expected_output': 'git init'
    },
    {
        'title': 'Добавление файлов',
        'slug': 'add',
        'order': 3,
        'content': '''
<h2>git add</h2>
<p>Команда <code>git add</code> добавляет файлы в область индексации (staging area) перед коммитом.</p>

<h3>Как использовать:</h3>
<pre><code>
git add filename.txt    # Добавить конкретный файл
git add .               # Добавить все файлы
git add *.py            # Добавить файлы по маске
</code></pre>

<h3>Пример:</h3>
<pre><code>
$ echo "print('Hello')" > main.py
$ git add main.py
$ git status
Changes to be committed:
  new file:   main.py
</code></pre>
''',
        'interactive_task': 'Добавьте файл main.py в индекс',
        'expected_output': 'git add main.py'
    },
    {
        'title': 'Создание коммита',
        'slug': 'commit',
        'order': 4,
        'content': '''
<h2>git commit</h2>
<p>Команда <code>git commit</code> сохраняет изменения из индекса в историю репозитория.</p>

<h3>Как использовать:</h3>
<pre><code>
git commit -m "Описание изменений"
git commit -am "Описание"  # Добавить и закоммитить все изменённые файлы
</code></pre>

<h3>Правила хорошего коммита:</h3>
<ul>
    <li>Краткое описание в настоящем времени</li>
    <li>Не более 50 символов в заголовке</li>
    <li>Подробности в теле коммита (если нужно)</li>
</ul>

<h3>Пример:</h3>
<pre><code>
$ git commit -m "Add main.py with hello world"
[main (root-commit) abc123] Add main.py with hello world
 1 file changed, 1 insertion(+)
 create mode 100644 main.py
</code></pre>
''',
        'interactive_task': 'Создайте коммит с сообщением "Initial commit"',
        'expected_output': 'git commit -m "Initial commit"'
    },
    {
        'title': 'Просмотр статуса',
        'slug': 'status',
        'order': 5,
        'content': '''
<h2>git status</h2>
<p>Команда <code>git status</code> показывает текущее состояние репозитория: какие файлы изменены, добавлены или ждут коммита.</p>

<h3>Как использовать:</h3>
<pre><code>git status</code></pre>

<h3>Что показывает:</h3>
<ul>
    <li>Текущую ветку</li>
    <li>Файлы в индексе (готовы к коммиту)</li>
    <li>Изменённые файлы (не в индексе)</li>
    <li>Неотслеживаемые файлы</li>
</ul>

<h3>Пример вывода:</h3>
<pre><code>
$ git status
On branch main
Changes to be committed:
  new file:   main.py
Changes not staged for commit:
  modified:   README.md
</code></pre>
''',
        'interactive_task': 'Проверьте статус репозитория',
        'expected_output': 'git status'
    },
    {
        'title': 'Просмотр истории',
        'slug': 'log',
        'order': 6,
        'content': '''
<h2>git log</h2>
<p>Команда <code>git log</code> показывает историю коммитов.</p>

<h3>Как использовать:</h3>
<pre><code>
git log              # Полная история
git log --oneline    # Кратко, по одной строке на коммит
git log -5           # Последние 5 коммитов
</code></pre>

<h3>Пример вывода:</h3>
<pre><code>
$ git log --oneline
abc1234 (HEAD -> main) Add main.py
def5678 Initial commit
</code></pre>

<p>Каждый коммит имеет уникальный хеш (abc1234), который можно использовать для возврата к этой версии.</p>
''',
        'interactive_task': 'Просмотрите историю коммитов в кратком формате',
        'expected_output': 'git log --oneline'
    },
    {
        'title': 'Работа с ветками',
        'slug': 'branch',
        'order': 7,
        'content': '''
<h2>git branch</h2>
<p>Ветки позволяют вести независимую разработку. Вы можете создавать новые ветки для экспериментов или новых функций.</p>

<h3>Основные команды:</h3>
<pre><code>
git branch              # Показать все ветки
git branch feature      # Создать новую ветку
git branch -d feature   # Удалить ветку
git checkout feature    # Переключиться на ветку
git checkout -b feature # Создать и переключиться
</code></pre>

<h3>Пример:</h3>
<pre><code>
$ git branch feature-login
$ git checkout feature-login
Switched to branch 'feature-login'
$ git branch
  main
* feature-login
</code></pre>
''',
        'interactive_task': 'Создайте новую ветку с именем feature',
        'expected_output': 'git branch feature'
    },
    {
        'title': 'Переключение между ветками',
        'slug': 'checkout',
        'order': 8,
        'content': '''
<h2>git checkout</h2>
<p>Команда <code>git checkout</code> переключает между ветками или восстанавливает файлы.</p>

<h3>Как использовать:</h3>
<pre><code>
git checkout branch-name      # Переключиться на ветку
git checkout -b new-branch    # Создать и переключиться
git checkout -- file.txt      # Отменить изменения в файле
</code></pre>

<h3>Важно:</h3>
<p>Перед переключением убедитесь, что все изменения закоммичены, иначе они могут быть потеряны.</p>

<h3>Пример:</h3>
<pre><code>
$ git checkout main
Switched to branch 'main'
$ git checkout -b develop
Switched to a new branch 'develop'
</code></pre>
''',
        'interactive_task': 'Переключитесь на ветку main',
        'expected_output': 'git checkout main'
    },
    {
        'title': 'Слияние веток',
        'slug': 'merge',
        'order': 9,
        'content': '''
<h2>git merge</h2>
<p>Команда <code>git merge</code> объединяет изменения из одной ветки в другую.</p>

<h3>Как использовать:</h3>
<pre><code>
git checkout main
git merge feature
</code></pre>

<h3>Типы слияния:</h3>
<ul>
    <li><strong>Fast-forward</strong> — если не было изменений в целевой ветке</li>
    <li><strong>Three-way merge</strong> — создаётся новый коммит слияния</li>
    <li><strong>Конфликт</strong> — требует ручного разрешения</li>
</ul>

<h3>Пример:</h3>
<pre><code>
$ git checkout main
$ git merge feature-login
Updating abc123..def456
Fast-forward
 login.py | 50 ++++++++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 50 insertions(+)
</code></pre>
''',
        'interactive_task': 'Слейте ветку feature в текущую ветку',
        'expected_output': 'git merge feature'
    },
    {
        'title': 'Отмена изменений',
        'slug': 'revert-reset',
        'order': 10,
        'content': '''
<h2>git revert и git reset</h2>
<p>Для отмены изменений используются команды <code>git revert</code> и <code>git reset</code>.</p>

<h3>git revert:</h3>
<pre><code>git revert HEAD      # Отменить последний коммит (создаёт новый коммит)</code></pre>
<p>Безопасно для опубликованных коммитов.</p>

<h3>git reset:</h3>
<pre><code>
git reset --soft HEAD~1   # Отменить коммит, оставить изменения в индексе
git reset --mixed HEAD~1  # Отменить коммит и индекс (по умолчанию)
git reset --hard HEAD~1   # Полностью отменить изменения
</code></pre>
<p>Опасно для опубликованных коммитов!</p>

<h3>Пример:</h3>
<pre><code>
$ git revert abc1234
[main def5678] Revert "Add main.py"
</code></pre>
''',
        'interactive_task': None,
        'expected_output': None
    },
    {
        'title': 'Удалённые репозитории',
        'slug': 'remote',
        'order': 11,
        'content': '''
<h2>git remote</h2>
<p>Команда <code>git remote</code> управляет удалёнными репозиториями (например, на GitHub).</p>

<h3>Основные команды:</h3>
<pre><code>
git remote -v              # Показать удалённые репозитории
git remote add origin url  # Добавить удалённый репозиторий
git remote remove origin   # Удалить удалённый репозиторий
</code></pre>

<h3>Пример:</h3>
<pre><code>
$ git remote add origin https://github.com/user/repo.git
$ git remote -v
origin  https://github.com/user/repo.git (fetch)
origin  https://github.com/user/repo.git (push)
</code></pre>
''',
        'interactive_task': 'Добавьте удалённый репозиторий с именем origin',
        'expected_output': 'git remote add origin https://github.com/user/repo.git'
    },
    {
        'title': 'Отправка изменений',
        'slug': 'push',
        'order': 12,
        'content': '''
<h2>git push</h2>
<p>Команда <code>git push</code> отправляет ваши коммиты в удалённый репозиторий.</p>

<h3>Как использовать:</h3>
<pre><code>
git push origin main         # Отправить ветку main
git push -u origin main      # Отправить и установить связь
git push --all               # Отправить все ветки
</code></pre>

<h3>Пример:</h3>
<pre><code>
$ git push origin main
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
To https://github.com/user/repo.git
   abc1234..def5678  main -> main
</code></pre>

<p>После первой отправки с флагом <code>-u</code> можно использовать просто <code>git push</code>.</p>
''',
        'interactive_task': 'Отправьте изменения в удалённый репозиторий',
        'expected_output': 'git push origin main'
    },
    {
        'title': 'Получение изменений',
        'slug': 'pull-fetch',
        'order': 13,
        'content': '''
<h2>git pull и git fetch</h2>
<p>Команды для получения изменений из удалённого репозитория.</p>

<h3>git fetch:</h3>
<pre><code>git fetch origin</code></pre>
<p>Загружает изменения, но не объединяет их с вашей работой.</p>

<h3>git pull:</h3>
<pre><code>git pull origin main</code></pre>
<p>Загружает изменения и сразу объединяет с текущей веткой (fetch + merge).</p>

<h3>Пример:</h3>
<pre><code>
$ git pull origin main
remote: Enumerating objects: 5, done.
From https://github.com/user/repo
   abc1234..def5678  main     -> origin/main
Updating abc1234..def5678
Fast-forward
 README.md | 3 +++
 1 file changed, 3 insertions(+)
</code></pre>
''',
        'interactive_task': 'Получите и объедините изменения из удалённого репозитория',
        'expected_output': 'git pull origin main'
    },
    {
        'title': 'Игнорирование файлов',
        'slug': 'gitignore',
        'order': 14,
        'content': '''
<h2>.gitignore</h2>
<p>Файл <code>.gitignore</code> указывает Git, какие файлы не нужно отслеживать.</p>

<h3>Пример .gitignore:</h3>
<pre><code>
# Лог файлы
*.log
logs/

# Временные файлы
*.tmp
*.cache

# Зависимости
node_modules/
venv/
__pycache__/

# Файлы окружения
.env
.env.local

# IDE
.vscode/
.idea/
</code></pre>

<h3>Правила:</h3>
<ul>
    <li><code>*</code> — любой символ</li>
    <li><code>/</code> в конце — только директории</li>
    <li><code>#</code> — комментарий</li>
    <li><code>!</code> — инверсия (не игнорировать)</li>
</ul>
''',
        'interactive_task': None,
        'expected_output': None
    },
    {
        'title': 'Конфликты слияния',
        'slug': 'conflicts',
        'order': 15,
        'content': '''
<h2>Разрешение конфликтов</h2>
<p>Конфликты возникают, когда одна и та же строка изменена в разных ветках.</p>

<h3>Как выглядит конфликт:</h3>
<pre><code>
<<<<<<< HEAD
old_value = 10
=======
old_value = 20
>>>>>>> feature
</code></pre>

<h3>Шаги разрешения:</h3>
<ol>
    <li>Откройте файл с конфликтом</li>
    <li>Выберите нужную версию кода (или объедините обе)</li>
    <li>Удалите маркеры конфликта (<code>&lt;&lt;&lt;&lt;&lt;</code>, <code>=======</code>, <code>&gt;&gt;&gt;&gt;&gt;</code>)</li>
    <li>Сохраните файл</li>
    <li>Добавьте файл: <code>git add file.txt</code></li>
    <li>Завершите слияние: <code>git commit</code></li>
</ol>

<h3>Совет:</h3>
<p>Используйте <code>git mergetool</code> для визуального разрешения конфликтов.</p>
''',
        'interactive_task': None,
        'expected_output': None
    }
]
