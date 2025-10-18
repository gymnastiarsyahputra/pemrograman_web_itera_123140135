document.addEventListener("DOMContentLoaded", () => {
  // === ELEMEN DOM ===
  const taskForm = document.getElementById("task-form");
  const taskNameInput = document.getElementById("task-name");
  const taskCourseInput = document.getElementById("task-course");
  const taskDeadlineInput = document.getElementById("task-deadline");
  const taskList = document.getElementById("task-list");
  const incompleteCountSpan = document.getElementById("incomplete-count");
  const searchInput = document.getElementById("search-input");
  const statusFilter = document.getElementById("status-filter");

  // === STATE APLIKASI ===
  // Memuat tugas dari localStorage atau menggunakan array kosong jika tidak ada
  let tasks = JSON.parse(localStorage.getItem("tasks")) || [];

  // === FUNGSI ===

  /**
   * Menyimpan array tasks ke localStorage setelah mengubahnya menjadi string JSON.
   */
  const saveTasks = () => {
    localStorage.setItem("tasks", JSON.stringify(tasks));
  };

  /**
   * Merender (menampilkan) daftar tugas ke halaman.
   * Fungsi ini membersihkan daftar yang ada, lalu membuat elemen HTML untuk setiap tugas.
   */
  const renderTasks = () => {
    taskList.innerHTML = ""; // Kosongkan daftar sebelum merender ulang

    // Filter tugas berdasarkan input pencarian dan status
    const searchTerm = searchInput.value.toLowerCase();
    const filterValue = statusFilter.value;

    const filteredTasks = tasks.filter((task) => {
      const matchesSearch =
        task.name.toLowerCase().includes(searchTerm) ||
        task.course.toLowerCase().includes(searchTerm);
      const matchesStatus =
        filterValue === "all" ||
        (filterValue === "completed" && task.isCompleted) ||
        (filterValue === "incomplete" && !task.isCompleted);
      return matchesSearch && matchesStatus;
    });

    if (filteredTasks.length === 0) {
      taskList.innerHTML = "<li>Tidak ada tugas yang sesuai.</li>";
    } else {
      filteredTasks.forEach((task) => {
        const li = document.createElement("li");
        li.className = `task-item ${task.isCompleted ? "completed" : ""}`;
        li.dataset.id = task.id;

        const deadlineDate = new Date(task.deadline);
        const formattedDeadline = deadlineDate.toLocaleDateString("id-ID", {
          year: "numeric",
          month: "long",
          day: "numeric",
          hour: "2-digit",
          minute: "2-digit",
        });
        li.innerHTML = `
                    <div class="task-info">
                        <input type="checkbox" class="complete-checkbox" ${
                          task.isCompleted ? "checked" : ""
                        }>
                        <div class="task-details">
                            <p>${task.name}</p>
                            <div>
                                <span>${task.course}</span>
                                <span>Deadline: ${task.deadline}</span>
                            </div>
                        </div>
                    </div>
                    <div class="task-actions">
                        <button class="btn-delete">Hapus</button>
                    </div>
                `;
        taskList.appendChild(li);
      });
    }
    updateIncompleteCount();
  };

  /**
   * Menambahkan tugas baru ke dalam array tasks.
   */
  const addTask = (name, course, deadline) => {
    // Validasi input
    if (name.trim() === "" || course.trim() === "" || deadline === "") {
      alert("Semua kolom wajib diisi!");
      return;
    }

    const newTask = {
      id: Date.now(), // ID unik berdasarkan timestamp
      name: name,
      course: course,
      deadline: deadline,
      isCompleted: false,
    };

    tasks.push(newTask);
    saveTasks();
    renderTasks();
  };

  /**
   * Menghapus tugas dari array tasks berdasarkan ID.
   */
  const deleteTask = (id) => {
    tasks = tasks.filter((task) => task.id !== id);
    saveTasks();
    renderTasks();
  };

  /**
   * Mengubah status selesai/belum selesai (toggle) pada tugas berdasarkan ID.
   */
  const toggleTaskComplete = (id) => {
    const task = tasks.find((task) => task.id === id);
    if (task) {
      task.isCompleted = !task.isCompleted;
      saveTasks();
      renderTasks();
    }
  };

  /**
   * Memperbarui tampilan jumlah tugas yang belum selesai.
   */
  const updateIncompleteCount = () => {
    const incompleteTasks = tasks.filter((task) => !task.isCompleted).length;
    incompleteCountSpan.textContent = incompleteTasks;
  };

  // === EVENT LISTENERS ===

  // Event listener untuk form penambahan tugas
  taskForm.addEventListener("submit", (e) => {
    e.preventDefault(); // Mencegah form dari reload halaman

    const taskName = taskNameInput.value;
    const taskCourse = taskCourseInput.value;
    const taskDeadline = taskDeadlineInput.value;

    addTask(taskName, taskCourse, taskDeadline);

    taskForm.reset(); // Mengosongkan form setelah submit
  });

  // Event listener untuk klik pada daftar tugas (untuk hapus dan tandai selesai)
  taskList.addEventListener("click", (e) => {
    const target = e.target;
    const parentLi = target.closest(".task-item");
    if (!parentLi) return;

    const taskId = Number(parentLi.dataset.id);

    if (target.classList.contains("btn-delete")) {
      deleteTask(taskId);
    } else if (target.classList.contains("complete-checkbox")) {
      toggleTaskComplete(taskId);
    }
  });

  // Event listener untuk filter dan pencarian
  searchInput.addEventListener("input", renderTasks);
  statusFilter.addEventListener("change", renderTasks);

  // === INISIALISASI ===
  // Render tugas yang ada saat halaman pertama kali dimuat
  renderTasks();
});
