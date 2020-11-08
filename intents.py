name = ''

def get_intent(data):
    m = data['message'].lower()
    if data['key']=="name":
        name = m
        return "next"
    
    if any( x in m for x in ['black soil properties','black','blacksoil','black soil']):
        return "black"
    elif any( x in m for x in ['red soil properties','red','redsoil','red soil']):
        return "red"
    elif any( x in m for x in ['aluvial soil properties','aluvial','aluvialsoil','aluvial soil']):
        return "aluvial"
    elif any( x in m for x in ['laterite soil properties','laterite','lateritesoil','laterite soil']):
        return "laterite"
    elif any( x in m for x in ['arid soil properties','arid','aridsoil','arid soil']):
        return "arid"
    elif any( x in m for x in 
                ['forest soil properties','forest','forestsoil','forest soil',
                    'mountain soil properties','mountain','mountainsoil','mountain soil']):
        return "forest"
    elif any( x in m for x in ['desert soil properties','desert','desertsoil','desert soil']):
        return "desert"
    else:
        return "invalid"
def handle(data):
    global name
    from flask import render_template
    intent = get_intent(data)

    if (intent == 'black'):
        return render_template('soils/blacksoil.html')
    elif intent == 'next' :
        return render_template('greet.html',
        name=name,
        question = {'key':'request','description':'what is the next task?'}
        )
    
    elif intent == 'red':
        return render_template('soils/redsoil.html')
    elif intent == 'arid':
        return render_template('soils/arid.html')
   
    elif intent == 'forest':
        return render_template('soils/forestsoil.html')
   
    elif intent == 'laterite':
        return render_template('soils/lateritesoil.html')
   
    elif intent == 'aluvial':
        return render_template('soils/aluvialsoil.html')
    elif intent == 'desert':
        return render_template('soils/desertsoil.html')
   
    else:
        return "Invalid"