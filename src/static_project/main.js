$(document).ready(function(){
    console.log('hello world')
    $('#skill_model_edit').click(function(){
        console.log('working')
        $('.ui.modal')
        .modal('show')
        ;
    })
    $('.ui.dropdown').dropdown()
})
document.querySelector('#name').addEventListener('input', function(e) {
    const location = document.querySelector('#location');
    if (e.target.value.length > 0) {
        location.required = true;
    } else {
        location.required = false;
    }
});

