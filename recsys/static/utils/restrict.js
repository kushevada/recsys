document.addEventListener("DOMContentLoaded", function() {
const restrictedButtons = document.querySelectorAll(".restricted");
restrictedButtons.forEach(button => {
    button.addEventListener("click", function(event) {
    event.preventDefault();
    alert("Ошибка: Чтобы получить рекомендации, войдите или зарегистрируйтесь на нашем сайте");
    });
});
});