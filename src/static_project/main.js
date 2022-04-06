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