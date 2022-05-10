$(document).ready(function(){

    console.log("Prueba")
    
    $('.hover').hover(function(){
        $(this).addClass('flip');
    },function(){
        $(this).removeClass('flip');
    });

    const btnswitch = document.querySelector('#switch');
    btnswitch.addEventListener('click' , () => {
    document.body.classList.toggle('dark');
    btnswitch.classList.toggle('active');

    if(document.body.classList.contains('dark')){
        localStorage.setItem('dark-mode', 'true');
    } else {
        localStorage.setItem('dark-mode', 'true');
    }    
    })


    if(localStorage.getItem('dark-mode') === 'true'){
        document.body.classList.add('dark');
        btnswitch.classList.add('active');    
    } else {
        document.body.classList.remove('dark');
        btnswitch.classList.remove('active');
    }

});

