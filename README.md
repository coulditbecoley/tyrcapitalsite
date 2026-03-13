<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Tyr Capital</title>

<style>

:root{
--bg:#07101c;
--bg-secondary:#0d1726;
--card:rgba(14, 24, 38, 0.88);
--text:#e8edf5;
--muted:#b8c2d3;
--accent:#c8a45a;
--border:rgba(255,255,255,0.08);
--shadow:0 18px 45px rgba(0,0,0,0.35);
--radius:22px;
}

*{
box-sizing:border-box;
}

body{
margin:0;
font-family:"Segoe UI","Helvetica Neue",Arial,sans-serif;
background:linear-gradient(180deg,#07101c 0%,#091423 45%,#0b1420 100%);
color:var(--text);
line-height:1.7;
}

.container{
width:min(1100px, calc(100% - 40px));
margin:0 auto;
}

header{

position:relative;
min-height:520px;
display:flex;
align-items:center;
justify-content:center;
text-align:center;
padding:40px 20px;

background-image:url("images/tyr-bg.png");
background-size:cover;
background-position:center;

border-bottom:1px solid rgba(255,255,255,0.06);

}

header::before{
content:"";
position:absolute;
inset:0;
background:linear-gradient(to bottom,rgba(4,10,18,0.55),rgba(4,10,18,0.82));
}

.hero-card{
position:relative;
z-index:2;
background:rgba(7,14,24,0.5);
border:1px solid rgba(255,255,255,0.08);
border-radius:28px;
padding:42px 32px;
box-shadow:var(--shadow);
}

h1{
margin:0;
font-size:clamp(3rem,6vw,4.8rem);
font-weight:700;
letter-spacing:2px;
}

main{
padding:70px 0 50px;
}

.section-card{
background:var(--card);
border:1px solid var(--border);
border-radius:var(--radius);
box-shadow:var(--shadow);
padding:34px 30px;
margin-bottom:28px;
}

h2{
margin:0 0 16px;
font-size:1.9rem;
font-weight:650;
color:var(--accent);
}

p{
margin:0 0 16px;
font-size:1.05rem;
color:var(--muted);
}

.image-wrap{
margin-top:20px;
}

.feature-image{
width:100%;
border-radius:20px;
box-shadow:0 16px 40px rgba(0,0,0,0.35);
border:1px solid rgba(255,255,255,0.08);
}

.contact-box{
display:inline-block;
margin-top:15px;
padding:14px 20px;
background:rgba(255,255,255,0.04);
border:1px solid rgba(255,255,255,0.08);
border-radius:16px;
color:#f3f6fb;
font-weight:600;
box-shadow:0 10px 25px rgba(0,0,0,0.25);
}

footer{
padding:10px 0 50px;
}

.footer-card{
background:rgba(10,18,30,0.92);
border:1px solid var(--border);
border-radius:18px;
box-shadow:var(--shadow);
padding:22px 24px;
color:#97a3b8;
font-size:0.92rem;
}

</style>
</head>

<body>

<header>

<div class="hero-card">
<h1>Tyr Capital</h1>
</div>

</header>

<main class="container">

<section class="section-card">

<h2>About Tyr Capital</h2>

<p>
Tyr Capital is a digital asset trading company focused on disciplined strategy development,
structured risk management, and market research across cryptocurrency markets.
</p>

<p>
Inspired by the Norse god Tyr, the company emphasizes discipline, consistency,
and long-term thinking when navigating the volatility of digital asset markets.
</p>

<div class="image-wrap">
<img src="images/tyr-bg.png" class="feature-image">
</div>

</section>


<section class="section-card">

<h2>Strategy</h2>

<p>
Tyr Capital studies market structure, technical analysis, and macro trends
to identify opportunities within cryptocurrency markets including Bitcoin
and other emerging digital asset sectors.
</p>

<p>
Capital preservation, disciplined execution, and risk-defined positioning remain
central principles behind every trading decision.
</p>

</section>


<section class="section-card">

<h2>Research</h2>

<p>
The firm publishes market observations and research covering cryptocurrency cycles,
macro developments, price structure, and evolving blockchain technologies.
</p>

</section>


<section class="section-card">

<h2>Contact</h2>

<p>
Join our Telegram Channel Tyr Capital Trades or Email for more information.
</p>

<div class="contact-box">
tyrcapitalllc@gmail.com
</div>

</section>

</main>


<footer class="container">

<div class="footer-card">

Disclaimer: Tyr Capital provides market research and commentary for informational
purposes only. Nothing on this website constitutes financial advice, investment advice,
or an offer to manage funds. Cryptocurrency markets involve substantial risk.

</div>

</footer>

</body>
</html>
