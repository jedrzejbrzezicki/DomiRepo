from flask import Flask, render_template_string

app = Flask(__name__)

# HTML Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rhythm Dance Academy</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
        }
        
        .navbar {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 1rem 2rem;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .navbar h1 {
            color: white;
            font-size: 1.8rem;
        }
        
        .hero {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-align: center;
            padding: 150px 20px 100px;
            margin-top: 60px;
        }
        
        .hero h2 {
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        
        .hero p {
            font-size: 1.3rem;
            margin-bottom: 2rem;
        }
        
        .btn {
            display: inline-block;
            padding: 12px 30px;
            background: white;
            color: #667eea;
            text-decoration: none;
            border-radius: 30px;
            font-weight: bold;
            transition: transform 0.3s;
        }
        
        .btn:hover {
            transform: scale(1.05);
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 60px 20px;
        }
        
        .section-title {
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 3rem;
            color: #667eea;
        }
        
        .classes-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 30px;
            margin-bottom: 40px;
        }
        
        .class-card {
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
            transition: transform 0.3s;
            text-align: center;
        }
        
        .class-card:hover {
            transform: translateY(-10px);
        }
        
        .class-card h3 {
            color: #667eea;
            font-size: 1.5rem;
            margin-bottom: 1rem;
        }
        
        .class-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        
        .about {
            background: #f8f9fa;
        }
        
        .schedule {
            background: white;
        }
        
        .schedule-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        
        .schedule-table th, .schedule-table td {
            padding: 15px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        
        .schedule-table th {
            background: #667eea;
            color: white;
        }
        
        .contact {
            background: #f8f9fa;
            text-align: center;
        }
        
        .contact-info {
            display: flex;
            justify-content: center;
            gap: 50px;
            flex-wrap: wrap;
            margin-top: 30px;
        }
        
        .contact-item {
            text-align: center;
        }
        
        .contact-item h4 {
            color: #667eea;
            margin-bottom: 10px;
        }
        
        footer {
            background: #333;
            color: white;
            text-align: center;
            padding: 20px;
        }
    </style>
</head>
<body>
    <nav class="navbar">
        <h1>🕺 Rhythm Dance Academy</h1>
    </nav>
    
    <section class="hero">
        <h2>Move to Your Rhythm</h2>
        <p>Discover the joy of dance with expert instructors</p>
        <a href="#contact" class="btn">Join Us Today</a>
    </section>
    
    <section class="container">
        <h2 class="section-title">Our Dance Classes</h2>
        <div class="classes-grid">
            <div class="class-card">
                <div class="class-icon">🩰</div>
                <h3>Ballet</h3>
                <p>Classic ballet technique for all ages. Build grace, strength, and discipline.</p>
            </div>
            <div class="class-card">
                <div class="class-icon">🎵</div>
                <h3>Hip Hop</h3>
                <p>High-energy street dance styles. Express yourself with urban moves.</p>
            </div>
            <div class="class-card">
                <div class="class-icon">💃</div>
                <h3>Salsa</h3>
                <p>Learn passionate Latin dance. Perfect for couples and singles alike.</p>
            </div>
            <div class="class-card">
                <div class="class-icon">🎭</div>
                <h3>Contemporary</h3>
                <p>Modern dance expression combining multiple styles and techniques.</p>
            </div>
        </div>
    </section>
    
    <section class="container about">
        <h2 class="section-title">About Us</h2>
        <p style="text-align: center; max-width: 800px; margin: 0 auto; font-size: 1.1rem;">
            Rhythm Dance Academy has been inspiring dancers for over 10 years. Our experienced instructors 
            are passionate about helping students of all levels discover their love for dance. Whether you're 
            a complete beginner or an experienced dancer, we have the perfect class for you.
        </p>
    </section>
    
    <section class="container schedule">
        <h2 class="section-title">Weekly Schedule</h2>
        <table class="schedule-table">
            <tr>
                <th>Day</th>
                <th>Time</th>
                <th>Class</th>
                <th>Level</th>
            </tr>
            <tr>
                <td>Monday</td>
                <td>6:00 PM - 7:30 PM</td>
                <td>Ballet</td>
                <td>Beginner</td>
            </tr>
            <tr>
                <td>Tuesday</td>
                <td>7:00 PM - 8:30 PM</td>
                <td>Hip Hop</td>
                <td>All Levels</td>
            </tr>
            <tr>
                <td>Wednesday</td>
                <td>6:30 PM - 8:00 PM</td>
                <td>Salsa</td>
                <td>Intermediate</td>
            </tr>
            <tr>
                <td>Thursday</td>
                <td>7:00 PM - 8:30 PM</td>
                <td>Contemporary</td>
                <td>Advanced</td>
            </tr>
            <tr>
                <td>Saturday</td>
                <td>10:00 AM - 11:30 AM</td>
                <td>Ballet</td>
                <td>Kids (Ages 6-12)</td>
            </tr>
        </table>
    </section>
    
    <section id="contact" class="container contact">
        <h2 class="section-title">Get In Touch</h2>
        <div class="contact-info">
            <div class="contact-item">
                <h4>📍 Location</h4>
                <p>123 Dance Street<br>Warsaw, Poland</p>
            </div>
            <div class="contact-item">
                <h4>📞 Phone</h4>
                <p>+48 123 456 789</p>
            </div>
            <div class="contact-item">
                <h4>✉️ Email</h4>
                <p>info@rhythmdance.com</p>
            </div>
        </div>
    </section>
    
    <footer>
        <p>&copy; 2024 Rhythm Dance Academy. All rights reserved.</p>
    </footer>
    
    <script>
        // Smooth scrolling for links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth' });
                }
            });
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True, port=5000)