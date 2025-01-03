// Load tasks from local storage when the page is loaded
window.onload = function() {
    loadTasks();
};

// Array to store tasks
let tasks = [];

// Function to add a task
function addTask() {
    const taskInput = document.getElementById("task-input");
    const taskText = taskInput.value.trim();

    if (taskText !== "") {
        // Create task object
        const newTask = {
            id: Date.now(),
            text: taskText
        };

        // Add task to tasks array
        tasks.push(newTask);

        // Save tasks to local storage
        saveTasks();

        // Clear input field
        taskInput.value = "";

        // Reload the task list
        loadTasks();
    }
}

// Function to load tasks from local storage and display them
function loadTasks() {
    // Get tasks from local storage
    const savedTasks = localStorage.getItem("tasks");

    if (savedTasks) {
        tasks = JSON.parse(savedTasks);
    }

    // Clear the existing task list
    const taskList = document.getElementById("task-list");
    taskList.innerHTML = "";

    // Display tasks
    tasks.forEach(task => {
        const taskItem = document.createElement("li");
        taskItem.setAttribute("data-id", task.id);

        const taskText = document.createElement("span");
        taskText.textContent = task.text;

        const editButton = document.createElement("button");
        editButton.className = "edit";
        editButton.textContent = "Edit";
        editButton.onclick = function() { editTask(task.id); };

        const deleteButton = document.createElement("button");
        deleteButton.className = "delete";
        deleteButton.textContent = "Delete";
        deleteButton.onclick = function() { deleteTask(task.id); };

        taskItem.appendChild(taskText);
        taskItem.appendChild(editButton);
        taskItem.appendChild(deleteButton);

        taskList.appendChild(taskItem);
    });
}

// Function to save tasks to local storage
function saveTasks() {
    localStorage.setItem("tasks", JSON.stringify(tasks));
}

// Function to delete a task
function deleteTask(taskId) {
    // Filter out the task with the given id
    tasks = tasks.filter(task => task.id !== taskId);

    // Save updated tasks to local storage
    saveTasks();

    // Reload the task list
    loadTasks();
}

// Function to edit a task
function editTask(taskId) {
    // Find the task to edit
    const taskToEdit = tasks.find(task => task.id === taskId);
    
    // Set the input field to the task's text
    const taskInput = document.getElementById("task-input");
    taskInput.value = taskToEdit.text;

    // Remove the task from the tasks array
    tasks = tasks.filter(task => task.id !== taskId);

    // Save updated tasks to local storage
    saveTasks();

    // Reload the task list
    loadTasks();

    // Set focus on the input field to edit the task
    taskInput.focus();
}
