// Storage Manager Class - ES6+ dengan Async/Await
class StorageManager {
    constructor(key) {
        this.key = key;
    }

    async save(data) {
        return new Promise((resolve) => {
            localStorage.setItem(this.key, JSON.stringify(data));
            resolve(true);
        });
    }

    async load() {
        return new Promise((resolve) => {
            const data = localStorage.getItem(this.key);
            resolve(data ? JSON.parse(data) : null);
        });
    }

    async delete() {
        return new Promise((resolve) => {
            localStorage.removeItem(this.key);
            resolve(true);
        });
    }
}

// Dashboard Class - menggunakan arrow functions dan template literals
class Dashboard {
    constructor() {
        this.profileStorage = new StorageManager('profile');
        this.tasksStorage = new StorageManager('tasks');
        this.notesStorage = new StorageManager('notes');
        this.tasks = [];
        this.notes = [];
        this.init();
    }

    async init() {
        await this.loadProfile();
        await this.loadTasks();
        await this.loadNotes();
        this.startClock();
        this.updateDate();
        this.loadWeather();
    }

    // Arrow function untuk clock
    startClock = () => {
        const updateTime = () => {
            const now = new Date();
            const hours = String(now.getHours()).padStart(2, '0');
            const minutes = String(now.getMinutes()).padStart(2, '0');
            const seconds = String(now.getSeconds()).padStart(2, '0');
            document.getElementById('clock').textContent = `${hours}:${minutes}:${seconds}`;
        };
        updateTime();
        setInterval(updateTime, 1000);
    }

    updateDate = () => {
        const now = new Date();
        const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
        const dateStr = now.toLocaleDateString('id-ID', options);
        document.getElementById('date').textContent = dateStr;
    }

    // Async function untuk load profile
    async loadProfile() {
        const profile = await this.profileStorage.load();
        if (profile) {
            document.getElementById('profileName').textContent = profile.name || '-';
            document.getElementById('profileEmail').textContent = profile.email || '-';
            document.getElementById('profileLocation').textContent = profile.location || '-';
        }
    }

    showProfileForm() {
        const name = prompt('Nama Anda:', document.getElementById('profileName').textContent);
        const email = prompt('Email Anda:', document.getElementById('profileEmail').textContent);
        const location = prompt('Lokasi Anda:', document.getElementById('profileLocation').textContent);
        
        if (name || email || location) {
            this.saveProfile({ name, email, location });
        }
    }

    async saveProfile(profile) {
        await this.profileStorage.save(profile);
        await this.loadProfile();
    }

    // Task Management dengan arrow functions
    async loadTasks() {
        this.tasks = await this.tasksStorage.load() || [];
        this.renderTasks();
    }

    renderTasks = () => {
        const taskList = document.getElementById('taskList');
        taskList.innerHTML = this.tasks.map((task, index) => `
            <li class="task-item">
                <span class="task-text">${task}</span>
                <button class="btn btn-delete" onclick="dashboard.deleteTask(${index})">Hapus</button>
            </li>
        `).join('');
    }

    async addTask() {
        const input = document.getElementById('taskInput');
        const task = input.value.trim();
        
        if (task) {
            this.tasks.push(task);
            await this.tasksStorage.save(this.tasks);
            input.value = '';
            this.renderTasks();
        }
    }

    async deleteTask(index) {
        this.tasks.splice(index, 1);
        await this.tasksStorage.save(this.tasks);
        this.renderTasks();
    }

    // Notes Management
    async loadNotes() {
        this.notes = await this.notesStorage.load() || [];
        this.renderNotes();
    }

    renderNotes = () => {
        const noteList = document.getElementById('noteList');
        noteList.innerHTML = this.notes.map((note, index) => `
            <div class="note-item">
                <div style="flex: 1;">
                    <strong>${note.title}</strong>
                    <p style="margin-top: 5px; color: #666;">${note.content}</p>
                </div>
                <button class="btn btn-delete" onclick="dashboard.deleteNote(${index})">Hapus</button>
            </div>
        `).join('');
    }

    async addNote() {
        const title = document.getElementById('noteTitle').value.trim();
        const content = document.getElementById('noteContent').value.trim();
        
        if (title && content) {
            this.notes.push({ title, content, date: new Date().toLocaleDateString('id-ID') });
            await this.notesStorage.save(this.notes);
            document.getElementById('noteTitle').value = '';
            document.getElementById('noteContent').value = '';
            this.renderNotes();
        }
    }

    async deleteNote(index) {
        this.notes.splice(index, 1);
        await this.notesStorage.save(this.notes);
        this.renderNotes();
    }

    // Weather dengan Promise
    async loadWeather() {
        try {
            // Simulasi API weather
            const weather = await new Promise(resolve => {
                setTimeout(() => {
                    const temps = [25, 27, 28, 30, 32];
                    const conditions = ['Cerah', 'Berawan', 'Hujan Ringan'];
                    resolve({
                        temp: temps[Math.floor(Math.random() * temps.length)],
                        condition: conditions[Math.floor(Math.random() * conditions.length)]
                    });
                }, 1000);
            });

            document.getElementById('temperature').textContent = `${weather.temp}°C`;
            document.getElementById('weatherDesc').textContent = weather.condition;
        } catch (error) {
            document.getElementById('weatherDesc').textContent = 'Tidak dapat memuat cuaca';
        }
    }
}

// Inisialisasi Dashboard
const dashboard = new Dashboard();
