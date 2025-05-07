
function openTeacherModal() {
    document.getElementById('teacherModal').style.display = 'flex';
}
function closeTeacherModal() {
    document.getElementById('teacherModal').style.display = 'none';
}

// Close modal when clicking outside
window.onclick = function(event) {
    const modal = document.getElementById('teacherModal');
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}

// Add Teacher button functionality
function addTeacher() {
    fetch('/addteacher')
        .then(response => response.text())
        .then(data => {
            main_page.innerHTML = data;

            const profilePictureInput = document.getElementById('profilePicture');
            const profileImage = document.getElementById('profileImage');
            const profilePreviewIcon = document.getElementById('profilePreview')?.querySelector('i');

            // 🖼️ Image preview
            profilePictureInput.addEventListener('change', function () {
                const file = this.files[0];
                if (file) {
                    const reader = new FileReader();
                    reader.onload = function (e) {
                        profileImage.src = e.target.result;
                        profileImage.style.display = 'block';
                        if (profilePreviewIcon) profilePreviewIcon.style.display = 'none';
                    };
                    reader.readAsDataURL(file);
                }
            });

            // Toggle status text
            document.getElementById('activeStatus').addEventListener('change', function () {
                document.getElementById('statusText').textContent = this.checked ? 'Active' : 'Inactive';
            });

            // Form submission
            document.getElementById('teacherRegistrationForm').addEventListener('submit', function (e) {
                e.preventDefault();

                let isValid = true;
                const fieldsToValidate = [
                    'firstName', 'lastName', 'level', 'tscNumber',
                    'idNumber', 'email', 'phone', 'password'
                ];

                // Reset errors
                document.querySelectorAll('.error-message').forEach(el => {
                    el.style.display = 'none';
                });

                // Validate required fields
                fieldsToValidate.forEach(field => {
                    const element = document.getElementById(field);
                    if (!element.value.trim() && field !== 'middleName') {
                        document.getElementById(`${field}-error`).textContent = 'This field is required';
                        document.getElementById(`${field}-error`).style.display = 'block';
                        isValid = false;
                    }
                });

                // Email format
                const email = document.getElementById('email');
                if (!/^\S+@\S+\.\S+$/.test(email.value)) {
                    document.getElementById('email-error').textContent = 'Invalid email format';
                    document.getElementById('email-error').style.display = 'block';
                    isValid = false;
                }
                // TSC number format
                const tscNumber = document.getElementById('tscNumber');
                if (!/^TSC\d{5,}$/.test(tscNumber.value)) {
                    document.getElementById('tscNumber-error').textContent = 'Invalid TSC number format';
                    document.getElementById('tscNumber-error').style.display = 'block';
                    isValid = false;
                }
                if (!isValid) return;

                // Prepare FormData for submission
                const formData = new FormData();
                formData.append("first_name", document.getElementById('firstName').value.trim());
                formData.append("second_name", document.getElementById('middleName').value.trim());
                formData.append("last_name", document.getElementById('lastName').value.trim());
                formData.append("level", document.getElementById('level').value);
                formData.append("gender", document.getElementById('gender').value);
                formData.append("email", email.value.trim());
                formData.append("phone_number", document.getElementById('phone').value.trim());
                formData.append("password", document.getElementById('password').value);
                formData.append("tsc_number", tscNumber.value.trim());
                formData.append("id_number", document.getElementById('idNumber').value.trim());
                formData.append("active_status", document.getElementById('activeStatus').checked ? 'active' : 'inactive');

                const profilePictureFile = profilePictureInput.files[0];
                if (profilePictureFile) {
                    formData.append("profile_picture", profilePictureFile);
                }

                // 🔄 Send the form data to backend
                fetch('/addteacher', {
                    method: 'POST',
                    body: formData
                })
                .then(response => response.json())
                .then(res => {
                    if (res.status) {
                        alert(res.message);
                        this.reset();
                        profileImage.style.display = 'none';
                        if (profilePreviewIcon) profilePreviewIcon.style.display = 'flex';
                    } else {
                        alert(res.message || "Something went wrong!");
                    }
                })
                .catch(err => {
                    console.error(err);
                    alert("An error occurred while submitting the form.");
                });
            });
        });
    }

//add student functionality 

function addStudent(){
    fetch('/addstudent').then(response => response.text()).then(data=>{
        main_page.innerHTML = data;
         // Profile picture preview
         document.getElementById('profilePicture').addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                // Validate file size (2MB max)
                if (file.size > 10 * 1024 * 1024) {
                    alert('File size exceeds 10MB limit');
                    this.value = '';
                    return;
                }
                
                const reader = new FileReader();
                reader.onload = function(event) {
                    const preview = document.getElementById('profilePreview');
                    const img = document.getElementById('profileImage');
                    const icon = preview.querySelector('i');
                    
                    img.src = event.target.result;
                    img.style.display = 'block';
                    icon.style.display = 'none';
                };
                reader.readAsDataURL(file);
            }
        });

        // Toggle active status
        document.getElementById('activeStatus').addEventListener('change', function() {
            document.getElementById('statusText').textContent = this.checked ? 'Active' : 'Inactive';
        });

        // Form submission
        document.getElementById('studentRegistrationForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Basic validation
            let isValid = true;
            const firstName = document.getElementById('firstName');
            const lastName = document.getElementById('lastName');
            const grade = document.getElementById('grade');
            const email = document.getElementById('email');
            const phone = document.getElementById('phone');
            const password = document.getElementById('password');
            const upa = document.getElementById('upa');
            
            // Reset error messages
            document.querySelectorAll('.error-message').forEach(el => el.style.display = 'none');
            
            // Validate required fields
            if (!firstName.value.trim()) {
                document.getElementById('firstName-error').textContent = 'First name is required';
                document.getElementById('firstName-error').style.display = 'block';
                isValid = false;
            }
            
            if (!lastName.value.trim()) {
                document.getElementById('lastName-error').textContent = 'Last name is required';
                document.getElementById('lastName-error').style.display = 'block';
                isValid = false;
            }
            
            if (!grade.value) {
                document.getElementById('grade-error').textContent = 'Grade is required';
                document.getElementById('grade-error').style.display = 'block';
                isValid = false;
            }
            
            if (!email.value.trim()) {
                document.getElementById('email-error').textContent = 'Email is required';
                document.getElementById('email-error').style.display = 'block';
                isValid = false;
            } else if (!/^\S+@\S+\.\S+$/.test(email.value)) {
                document.getElementById('email-error').textContent = 'Please enter a valid email';
                document.getElementById('email-error').style.display = 'block';
                isValid = false;
            }
            
            if (!phone.value.trim()) {
                document.getElementById('phone-error').textContent = 'Phone number is required';
                document.getElementById('phone-error').style.display = 'block';
                isValid = false;
            }
            
            if (!password.value) {
                document.getElementById('password-error').textContent = 'Password is required';
                document.getElementById('password-error').style.display = 'block';
                isValid = false;
            } else if (password.value.length < 6) {
                document.getElementById('password-error').textContent = 'Password must be at least 6 characters';
                document.getElementById('password-error').style.display = 'block';
                isValid = false;
            }
            
            if (isValid) {
                const form = document.getElementById('studentRegistrationForm');
                const formData = new FormData(form); // Automatically collects all form inputs
                const imageFile = document.getElementById('profilePicture').files[0];
                if (imageFile) {
                    formData.append('profile_picture', imageFile); // Attach file to FormData
                }
            
                fetch('/addstudent', {
                    method: 'POST',
                    body: formData
                })
                .then(response => response.json())
                .then(result => {
                    if (result.status) {
                        alert('Student registered successfully!');
                        form.reset();
                        document.getElementById('profileImage').style.display = 'none';
                        document.getElementById('profilePreview').querySelector('i').style.display = 'flex';
                    } else {
                        alert('Failed: ' + result.message);
                    }
                });
            }
            
        });
    });  
    
}