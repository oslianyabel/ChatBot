from flask import session
import random

def generate_response(message):
    #start
    if 'hola' in message.lower() or session.get('state') == 'start':
        msg = "Hola, para derivarte al departamento pertinente, selecciona una de estas cuentas: (1)->Atención al cliente.    (2)->Marketing."
        session['state'] = 'departamento'
        return msg
    elif 'adios' in message.lower():
        session['state'] = 'start'
        return "¡Hasta luego!"
    #departamento
    elif session.get('state') == 'departamento':
        if message == '1':
            msg = 'Hola soy Maria, te puedo ayudar con lo siguiente: (1)->Consulta estado pedido. (2)->Devoluciones. (3)->Garantía. (4)->Repuestos. (5)->Información producto. (6)->Compatibilidades. (7)->Software (8)->Entrada de stock'
            session['state'] = 'atencion al cliente'
            return msg
        if message == '2':
            msg = 'Hola soy Laura, te puedo ayudar con lo siguiente: (1)->Patrocinios / eventos e-sport. (2)->Colaboraciones. (3)->Merchandising. (4)->Otros.'
            session['state'] = 'no info'
            return msg
        else:
            return 'Entrada invalida'
    #atencion al cliente
    elif session.get('state') == 'atencion al cliente':
        if message == '1':
            msg = 'me puedes proporcionar tu número de pedido? (ponga "si" en caso de ser valido)'
            session['state'] = 'estado del pedido'
            return msg
        if message == '2' or message == '3':
            msg = 'Vale, ante todo te pedimos disculpas por todas las molestias causadas. Podrías indicarme el número de pedido?'
            session['state'] = 'devoluciones'
            return msg
        if message == '4' or message == '5' or message == '6' or message == '7' or message == '8':
            return 'Flujo con retroalimentacion de odoo'
        else:
            return 'Entrada invalida'
    #estado del pedido
    elif session.get('state') == 'estado del pedido':
        if message.lower() == 'si':
            msg = 'Lo acabo de encontrar, aquí lo tienes. [Información del estado del pedido.]'
            session['state'] = 'start'
            return msg
        else:
            msg = 'No encuentro tu pedido, me puedes dar un poco dar un poco más de información y en este orden por favor: Nombre completo, Dirección de entrega, Email de contacto (ponga "si" para avanzar el flujo)'
            session['state'] = 'estado del pedido 2'
            return msg
    elif session.get('state') == 'estado del pedido 2':
        if message.lower() == 'si':
            msg = '[Información del estado del pedido.]'
            session['state'] = 'start'
            return msg
        else:
            msg = 'No hemos podido localizar tu pedido. Hemos facilitado la información a los compañeros para que puedan ponerse en contacto contigo.'
            session['state'] = 'start'
            return msg
    #devoluciones
    elif session.get('state') == 'devoluciones':
        msg = 'Cual es el motivo de la devolución, escribe el número que sea tu caso: (1)->No lo quiero. (2)->Fallo'
        session['state'] = 'motivo'
        return msg
    #motivo
    elif session.get('state') == 'motivo':
        if message == '1':
            rand = random.random()
            if rand < 0.4:
                msg = 'En este caso al tratarse de un producto que está en perfectas condiciones pero ya no deseas, tendrías que hacerte cargo de los portes y enviarlo bien protegido a la siguiente dirección indicando el nombre al que se realizó la compra: - Biomag SL, (Mars Gaming) - C/ Barrachi 39, Local 3, 01013 - Vitoria (Álava) - ATT. Javi Y una vez lo recibamos procederemos con el reembolso del pedido'
                session['state'] = 'start'
                return msg
            else:
                msg = 'Lamentamos comunicarte que tu pedido se encuentra fuera del plazo de devolución. Quieres hablar con uno de nuestros técnicos?'
                session['state'] = 'tecnicos'
                return msg
        if message == '2':
            msg = 'Me aparece operación no válida, esto se debe a que no encuentra el pedido o ya no esta en garantía.'
            session['state'] = 'start'
            return msg
        else:
            return 'Entrada invalida'
    #tecnicos
    elif session.get('state') == 'tecnicos':
        if message == 'si':
            msg = 'El ticket se ha creado, tendrás un correo en las próximas 48 horas.'
            session['state'] = 'start'
            return msg
        if message == 'no':
            msg = 'Muchas gracias por contactarnos!'
            session['state'] = 'start'
            return msg
        else:
            return 'Entrada invalida'
    elif session.get('state') == 'no info':
        return 'Fin del diagrama de flujo'
    else:
        msg = 'Hola, para derivarte al departamento pertinente, selecciona una de estas cuentas: (1)->Atención al cliente.    (2)->Marketing.'
        session['state'] = 'departamento'
        return msg
        
    
        