from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html><head><meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Khairiyyerh's Food Corner - Katsina</title>
    <style>
    body{font-family:sans-serif;background:#fff8e1;padding:10px;margin:0}
    .header{background:linear-gradient(135deg,#e65100,#ff8f00);color:white;padding:18px;border-radius:15px;max-width:430px;margin:auto auto 12px auto;text-align:center}
    .grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;max-width:430px;margin:auto}
    .card{background:white;padding:10px;border-radius:16px;box-shadow:0 3px 12px rgba(0,0,0,0.08);text-align:center}
    .card img{width:100%;height:90px;border-radius:10px;object-fit:cover}
    .price{color:#2e7d32;font-weight:bold;font-size:16px;margin:4px 0}
    .btn{background:#25D366;color:white;padding:6px 12px;border-radius:20px;text-decoration:none;font-size:11px;font-weight:bold;display:inline-block;margin-top:5px}
    .footer{max-width:430px;margin:20px auto;text-align:center;background:white;padding:15px;border-radius:15px}
    </style></head><body>
    <div class="header"><h2 style="margin:0">Khairiyyerh's Food Corner 🍲</h2><p style="margin:5px 0 0 0;font-size:13px">📍 KATSINA | 0901 569 8498</p></div>
    <div class="grid">
    <div class="card"><img src="https://images.unsplash.com/photo-1585937421612-70a008356fbe"><h3 style="margin:8px 0 2px 0;font-size:14px">Hot Awara</h3><div class="price">₦2,000</div><a class="btn" href="https://wa.me/2349015698498?text=Salam%20I%20want%20Awara%202000">Order</a></div>
    <div class="card"><img src="https://images.unsplash.com/photo-1574323347407-f5e1ad6d020b"><h3 style="margin:8px 0 2px 0;font-size:14px">Waina Flour</h3><div class="price">₦700</div><a class="btn" href="https://wa.me/2349015698498?text=Salam%20I%20want%20Waina%20Flour%20700">Order</a></div>
    <div class="card"><img src="https://images.unsplash.com/photo-1565557623262-b51c2513a641"><h3 style="margin:8px 0 2px 0;font-size:14px">Gullisuwa</h3><div class="price">₦1,500</div><a class="btn" href="https://wa.me/2349015698498?text=Salam%20I%20want%20Gullisuwa%201500">Order</a></div>
    <div class="card"><img src="https://images.unsplash.com/photo-1544148103-0772bf10d330"><h3 style="margin:8px 0 2px 0;font-size:14px">Kunun Aya 🥤</h3><div class="price">₦500</div><a class="btn" href="https://wa.me/2349015698498?text=Salam%20I%20want%20Kunun%20Aya%20500">Order</a></div>
    </div>
    <div class="footer"><p style="font-size:12px;color:#555;margin:0">📍 Katsina, Katsina State</p><p style="font-size:12px;color:#555;margin:3px 0">📞 0901 569 8498</p><a class="btn" style="padding:12px 22px;font-size:13px;margin-top:12px" href="https://wa.me/2349015698498?text=Salam%20Khairiyyerh's%20Food%20Corner%20Katsina%20I%20want%20to%20order">💬 Order on WhatsApp</a></div>
    </body></html>
    """
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
