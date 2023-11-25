function togglePassword() {
    var passwordInput = document.getElementById('password');
    var passwordToggleBtn = document.querySelector('.password-toggle-btn');
  
    if (passwordInput.type === 'password') {
      passwordInput.type = 'text';
      passwordToggleBtn.textContent = '👁️';
    } else {
      passwordInput.type = 'password';
      passwordToggleBtn.textContent = '👁️';
    }
  }
  