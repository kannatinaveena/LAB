const form = document.getElementById('registrationForm');
const message = document.getElementById('message');

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const formData = {
    name: form.name.value,
    email: form.email.value,
    password: form.password.value
  };

  try {
    const response = await fetch('/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData)
    });

    if (response.ok) {
      message.textContent = 'Registration successful!';
      form.reset();
    } else {
      message.textContent = 'Registration failed. Try again.';
    }
  } catch (error) {
    message.textContent = 'An error occurred. Please try again.';
  }
});
