// Установка csrf_token
(function () {
    let csrftoken = Cookies.get('csrftoken');
    $.ajaxSetup({
        headers: {"X-CSRFToken": csrftoken}
    });
})();

// Показать форму комментария
let openForm = function (id) {
    $(`#${id}`).show()
};
// Скрыить форму комментария
let closeForm = function (id) {
    $(`#${id}`).hide()
};
let update = function (id) {
    $.ajax({
        url: "http://127.0.0.1:8000/api/v1/app/post/detail/"+ id+'/',
        type: "GET",
        data: {
            pk:id,
        },
        success: (response) => {
            window.location = response
        },
        error: (response) => {
            console.log("False")
         }

    });
};
// Поставить лайк
let like = function (id) {
    $.ajax({
        url: "http://127.0.0.1:8000/like/",
        type: "POST",
        data: {
            pk: id,
        },
        success: (response) => {
            window.location = response
        },
        error: (response) => {
            console.log("False")
         }

    });
};
