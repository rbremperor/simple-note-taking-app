document.addEventListener("DOMContentLoaded", function () {
    const modal = document.getElementById("modal");
    const overlay = document.getElementById("overlay");
    window.openModal = function () {
        modal.style.display = "block";
        overlay.style.display = "block";
    };

    window.closeModal = function () {
        modal.style.display = "none";
        overlay.style.display = "none";
    };

    overlay.addEventListener("click", closeModal);

});

document.addEventListener("DOMContentLoaded", function () {
    const overlay = document.getElementById("overlay");
    const updateModal = document.getElementById("update-modal");
    const updateForm = document.getElementById("update-form");

    window.openUpdateModal = function (taskId, title, content) {
    console.log("Opening modal for:", taskId, title, content);

    document.getElementById("update-task-id").value = taskId;
    document.getElementById("update-title").value = title;
    document.getElementById("update-content").value = content;

    // Fix: Dynamically set form action
    document.getElementById("update-form").action = `/update-task/${taskId}/`;

    document.getElementById("update-modal").style.display = "block";
    document.getElementById("overlay").style.display = "block";
};


    window.closeUpdateModal = function () {
        updateModal.style.display = "none";
        overlay.style.display = "none";
    };

    overlay.addEventListener("click", closeUpdateModal);
});
document.getElementById("update-form").addEventListener("submit", function (event) {
    console.log("🚀 Update button clicked!");
});
