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
