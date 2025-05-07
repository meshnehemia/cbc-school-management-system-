let nav_items = document.getElementsByClassName('nav-item');
let main_page = document.getElementById('main-content');
Array.from(nav_items).forEach(button => {
    button.addEventListener('click', (event) => {
        Array.from(nav_items).forEach(btn => btn.classList.remove('active'));
        button.classList.add('active');
        
        if(button.id == 'students'){
            fetch('/studentsmanagement').then(response => response.text()).then(data=>{
                    main_page.innerHTML = data;
                    // Student Modal functionality
                    function openStudentModal() {
                        document.getElementById('studentModal').style.display = 'flex';
                    }
                    function closeStudentModal() {
                        document.getElementById('studentModal').style.display = 'none';
                    }
                    // Close modal when clicking outside
                    window.onclick = function(event) {
                        const modal = document.getElementById('studentModal');
                        if (event.target == modal) {
                            modal.style.display = 'none';
                        }
                    }
                    // Tab functionality
                    function openTab(evt, tabName) {
                        const tabContents = document.getElementsByClassName('tab-content');
                        for (let i = 0; i < tabContents.length; i++) {
                            tabContents[i].classList.remove('active');
                        }

                        const tabs = document.getElementsByClassName('tab');
                        for (let i = 0; i < tabs.length; i++) {
                            tabs[i].classList.remove('active');
                        }

                        document.getElementById(tabName).classList.add('active');
                        evt.currentTarget.classList.add('active');
                    }
            });  
        }else if(button.id == 'teachers'){
            fetch('/teachersManagement').then(response => response.text()).then(data=>{
                    main_page.innerHTML = data;
            });  
        }else if(button.id == 'curriculum'){
            fetch('/curriculum').then(response => response.text()).then(data=>{
                    main_page.innerHTML = data;
                    const strandHeaders = document.querySelectorAll('.strand-header');
                    strandHeaders.forEach(header => {
                        header.addEventListener('click', () => {
                            const content = header.nextElementSibling;
                            const icon = header.querySelector('i');
                            
                            content.classList.toggle('open');
                            if (content.classList.contains('open')) {
                                icon.classList.remove('fa-chevron-down');
                                icon.classList.add('fa-chevron-up');
                            } else {
                                icon.classList.remove('fa-chevron-up');
                                icon.classList.add('fa-chevron-down');
                            }
                        });
                    });
            
                    // Grade selector functionality
                    const gradeBtns = document.querySelectorAll('.grade-btn');
                    gradeBtns.forEach(btn => {
                        btn.addEventListener('click', () => {
                            gradeBtns.forEach(b => b.classList.remove('active'));
                            btn.classList.add('active');
                            // Here you would load the appropriate grade content
                        });
                    });
            });  
        }else if(button.id == 'reports'){
            fetch('/reports').then(response => response.text()).then(data=>{
                    main_page.innerHTML = data;
                    
            });  
        }else if(button.id == 'assessments'){
            fetch('/assessments').then(response => response.text()).then(data=>{
                    main_page.innerHTML = data;
                    // Modal functionality
                    const modal = document.getElementById("newAssessmentModal");
                    const btn = document.getElementById("newAssessmentBtn");
                    const span = document.getElementsByClassName("close-btn")[0];

                    btn.onclick = function() {
                        modal.style.display = "flex";
                    }

                    span.onclick = function() {
                        modal.style.display = "none";
                    }

                    window.onclick = function(event) {
                        if (event.target == modal) {
                            modal.style.display = "none";
                        }
                    }

                    // Tab functionality
                    const tabs = document.querySelectorAll(".tab");
                    tabs.forEach(tab => {
                        tab.addEventListener("click", () => {
                            tabs.forEach(t => t.classList.remove("active"));
                            tab.classList.add("active");
                            // Here you would load the appropriate content for the tab
                        });
                    });
            });  
        }else if(button.id == 'performance'){
            fetch('/perfomance').then(response => response.text()).then(data=>{
                    main_page.innerHTML = data;
                    // Sample JavaScript for interactive elements
                    document.querySelectorAll('.competency-card').forEach(card => {
                        card.addEventListener('click', () => {
                            // Implement detailed competency view
                            alert('Detailed competency view would open here');
                        });
                    });
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
                 // Update status select colors based on selection
                document.querySelectorAll('.status-select').forEach(select => {
                    select.addEventListener('change', function() {
                        this.className = `status-select ${this.value}`;
                    });
                });

                // Save attendance handler
                document.querySelector('.save-button').addEventListener('click', () => {
                    alert('Attendance saved successfully!');
                    // Add actual save logic here
                });
            });  
        }
    });
});

