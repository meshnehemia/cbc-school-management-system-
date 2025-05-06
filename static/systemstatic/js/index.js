let nav_items = document.getElementsByClassName('nav-item');
let main_page = document.getElementById('main-content');
Array.from(nav_items).forEach(button => {
    button.addEventListener('click', (event) => {
        Array.from(nav_items).forEach(btn => btn.classList.remove('active'));
        button.classList.add('active');
        
        if(button.id == 'students'){
            fetch('/studentsmanagement').then(response => response.text()).then(data=>{
                    main_page.innerHTML = data;
            });  
        }else if(button.id == 'teachers'){
            fetch('/teachersManagement').then(response => response.text()).then(data=>{
                    main_page.innerHTML = data;
            });  
        }else if(button.id == 'curriculum'){
            fetch('/curriculum').then(response => response.text()).then(data=>{
                    main_page.innerHTML = data;
            });  
        }else if(button.id == 'reports'){
            fetch('/reports').then(response => response.text()).then(data=>{
                    main_page.innerHTML = data;
            });  
        }else if(button.id == 'assessments'){
            fetch('/assessments').then(response => response.text()).then(data=>{
                    main_page.innerHTML = data;
            });  
        }else if(button.id == 'performance'){
            fetch('/perfomance').then(response => response.text()).then(data=>{
                    main_page.innerHTML = data;
            });  
        }else if(button.id == 'timetable'){
            fetch('/studentsattendance').then(response => response.text()).then(data=>{
                    main_page.innerHTML = data;
            });  
        }else if(button.id == 'dashboard'){
            window.location.href = '/';
        }else if(button.id == 'finances'){
            fetch('/finances').then(response => response.text()).then(data=>{
                main_page.innerHTML = data;
        }); 
        }else{
            fetch('/studentsattendance').then(response => response.text()).then(data=>{
                main_page.innerHTML = data;
            });  
        }
    });
});
