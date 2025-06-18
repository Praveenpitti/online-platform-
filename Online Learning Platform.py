<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>LearnZone - Online Learning Platform</title>
  <style>
    body {
      margin: 0;
      font-family: 'Segoe UI', sans-serif;
      background: #f0f0f0;
      color: #333;
      padding: 20px;
    }

    header {
      text-align: center;
      background: #4a90e2;
      color: white;
      padding: 20px;
      border-radius: 8px;
    }

    video {
      width: 100%;
      max-width: 800px;
      margin: 20px auto;
      display: block;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0,0,0,0.2);
    }

    section {
      max-width: 800px;
      margin: 0 auto;
    }

    .quiz {
      background: white;
      padding: 20px;
      border-radius: 10px;
      margin-top: 20px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }

    .quiz h3 {
      margin-top: 0;
    }

    .progress {
      margin-top: 20px;
      background: #ddd;
      border-radius: 20px;
      overflow: hidden;
    }

    .progress-bar {
      background: #4caf50;
      height: 20px;
      width: 0%;
      text-align: center;
      color: white;
    }

    button {
      padding: 10px 20px;
      background: #4a90e2;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      margin-top: 10px;
    }

    button:hover {
      background: #357abd;
    }
  </style>
</head>
<body>
  <header>
    <h1>LearnZone</h1>
    <p>Welcome to your interactive learning journey!</p>
  </header>

  <section>
    <video controls>
      <source src="https://www.w3schools.com/html/mov_bbb.mp4" type="video/mp4">
      Your browser does not support video playback.
    </video>

    <div class="quiz">
      <h3>Quick Quiz: What does HTML stand for?</h3>
      <label><input type="radio" name="q1" value="wrong"> HighText Machine Language</label><br>
      <label><input type="radio" name="q1" value="right"> HyperText Markup Language</label><br>
      <label><input type="radio" name="q1" value="wrong"> HyperText Markdown Link</label><br>
      <button onclick="submitQuiz()">Submit Answer</button>
      <p id="quizResult"></p>
    </div>

    <div class="progress">
      <div class="progress-bar" id="progressBar">0%</div>
    </div>
  </section>

  <script>
    // Progress tracking
    function updateProgressBar(percent) {
      const bar = document.getElementById('progressBar');
      bar.style.width = percent + '%';
      bar.textContent = percent + '%';
      localStorage.setItem('progress', percent);
    }

    function loadProgress() {
      const saved = localStorage.getItem('progress');
      if (saved) updateProgressBar(saved);
    }

    function submitQuiz() {
      const selected = document.querySelector('input[name="q1"]:checked');
      if (!selected) {
        alert("Please select an answer.");
        return;
      }

      const result = document.getElementById('quizResult');
      if (selected.value === 'right') {
        result.textContent = "✅ Correct!";
        updateProgressBar(100);
      } else {
        result.textContent = "❌ Try again.";
        updateProgressBar(50);
      }
    }

    // Load stored progress on page load
    loadProgress();
  </script>
</body>
</html>
