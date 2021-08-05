RUN_STRINGS = (
    "¿A dónde crees que vas?",
    "Eh? qué? ¿Se han ido?",
    "ZZzzZZzz... Eh? Qué? oh, otra vez, no importa.",
    "Vuelve aquí!",
    "No tan rápido...",
    "Cuidado con la pared!",
    "No me dejes sola con ellos!!",
    "Si corres, mueres.",
    "Te jodes, estoy en todas partes",
    "Te vas a arrepentir de eso...",
    "Tambien puedes probar con /kickme, Creo que es divertido.",
    "Vete a quejarte a otro lado, no le importa a nadie aquí.",
    "Puedes correr, pero no puedes esconderte.",
    "¿Es todo lo que tienes?",
    "Estoy detras de ti...",
    "Tienes compañia!",
    "Podemos hacer esto por las buenas o por las malas.",
    "No lo has entendido, no?",
    "Si eso, mejor corre.",
    "Por favor, recuerdame lo mucho que me importa.",
    "Yo correría más rápido si fuese tú.",
    "Ese es definitivamente el androide que estamos buscando.",
    "Que la suerte esté de tu parte.",
    "Famosas últimas palabras.",
    "Y desaparecieron para siempre, para nunca volver a ser vistos.",
    "\"Oh, mírame! Qué guay soy, puedo escaparme de un bot!\" - esta persona",
    "Si, si, escribe /kickme a ver.",
    "Toma, toma este anillo y dirígete a Mordor mientras estás en ello.",
    "Las leyendas lo tienen, aún están funcionando...",
    "A diferencia de Harry Potter, tus padres no pueden protegerte de mí.",
    "El miedo lleva a la ira. La ira lleva al odio. El odio conduce al sufrimiento. Si sigues corriendo con miedo, podrías "
    "ser el próximo Vader.",
    "Después de muchos cálculos, he llegado a la conclusión de que mi interés en tus mierdas es 0.",
    "Las leyendas lo cuentan, aun siguen funcionando.",
    "Sigue así, no estoy segura de que te queramos aquí de todos modos.",
    "Eres un mag- Oh. Espera. No eres Harry, prosigue.",
    "NO SE CORRE EN LOS PASILLOS",
    "Hasta la vista, baby.",
    "Who let the dogs out?",
    "Es gracioso porque a nadie le importa.",
    "Ah, qué desperdicio. Este me gustaba.",
    "Frankly, cariño, Me importa una mierda.",
    "Mi batido trae a todos los niños al patio ... Así que corre más rápido!",
    "No puedes soportar la verdad!",
    "Hace mucho tiempo, en una galaxia muy lejana ... A alguien le habría importado eso. Aunque ya no.",
    "Hey, míralos! Se están escapando del inevitable ban... Qué monos.",
    "Han dispara primero. Yo también.",
    "¿De que te escapas?¿De un conejo blanco?",
    "Como diria El Doctor...Corre!",
)

SLAP_TEMPLATES = (
    "{user1} {hits} a {user2} con {item}.",
    "{user1} {hits} a {user2} en la cara con {item}.",
    "{user1} {hits} a {user2} en el pecho con {item}.",
    "{user1} {throws} {item} a {user2}.",
    "{user1} {throws} a la cara {item} a {user2} .",
    "{user1} lanza a la cabeza {item} a {user2}.",
    "{user1} empieza a abofetear a {user2} con {item}.",
    "{user1} derriba a {user2} y repetidas veces le {hits} con {item}.",
    "{user1} coge {item} y {hits} a {user2}.",
    "{user1} ata a {user2} a una silla y {throws} {item}.",
    "{user1} le ha dado un amistoso empujón a {user2} para que aprenda a nadar en lava."
)

ITEMS = (
    "una sartén de metal",
    "una trucha",
    "un bate de béisbol",
    "un bate de cricket",
    "un bastón de madera",
    "una uña",
    "una impresora",
    "una pala",
    "un proyector",
    "un libro de física",
    "una tostadora",
    "un retrato del Fary",
    "una televisión",
    "un camión de 5 toneladas",
    "un tubo lleno de heces",
    "un libro",
    "un portátil",
    "una tortuga muerta",
    "un saco de piedras",
    "un calzoncillo usado",
    "un pollo de goma",
    "un consolador gigante",
    "un extintor",
    "un trozo de mierda petrificado",
    "una batidora",
    "un papel en llamas",
    "un trozo de carne",
    "un oso",
    "una vaca",
)

THROW = (
    "le tira",
    "le lanza",
    "le arroja",
    "le tira",
)

HIT = (
    "golpea",
    "abofetea",
    "atiza",
    "casca",
    "sacude",
)

MARKDOWN_HELP = """
Markdown es una herramienta de formato muy poderosa soportada por telegram. {} tiene algunas mejoras, para asegurarse de que \
las notas guardadas se analizan correctamente y te permiten crear botones..
- <code>_cursiva_</code>: si se introduce el texto entre '_' generará texto en cursiva
- <code>*negrita*</code>: si se introduce el texto entre '*' generará texto en negrita
- <code>`codigo`</code>: si se introduce el texto entre '`' generará texto monoespaciado, también conocido como 'código'
- <code>[algúntexto](algunaURL)</code>: esto creará un link - el mensaje se mostrará en <code>algúntexto</code>, \
y pulsando en el te llevará a la página que has puesto en <code>algunaURL</code>.
EJ: <code>[test](example.com)</code>
- <code>[textodelboton](buttonurl:algunaURL)</code>: esta es una mejora especial que permite a los usuarios \
tener botones de telegram. <code>textodelboton</code> será el nombre que aparezca en el botón, y <code>algunaURL</code> \
será la página web o URL que se abrirá al pulsar.
EG: <code>[Esto es un botón](buttonurl:example.com)</code>
Si quieres poner varios botones en la misma línea, usa :same, como aquí:
<code>[uno](buttonurl://example.com)
[dos](buttonurl://google.com:same)</code>
Esto creará dos botones en la misma línea en vez de uno en cada línea.
"""

SpanishStrings = {

#Connections
    "Disabled connections to this chat for users": "Conexiones deshabilitadas en este chat para los usuarios",
    "Enabled connections to this chat for users": "Conexiones habilitadas en este chat para los usuarios",
    "Please enter on/yes/off/no in group!": "Por favor escribe on/yes/off/no en el grupo!",
    "Successfully connected to *{}*": "Conectado correctamente a *{}*",
    "Connection failed!": "Conexión fallida!",
    "Connections to this chat not allowed!": "Conexiones no permitidas en este chat!",
    "Write chat ID to connect!": "Escribe el ID del chat para conectar!",
    "Usage limited to PMs only!": "Uso restringido solo a mensajes privados",

#Misc
    "RUNS-K": RUN_STRINGS,
    "SLAP_TEMPLATES-K": SLAP_TEMPLATES,
    "ITEMS-K": ITEMS,
    "HIT-K": HIT,
    "THROW-K": THROW,
    "ITEMP-K": ITEMS,
    "ITEMR-K": ITEMS,
    "MARKDOWN_HELP-K": MARKDOWN_HELP,

    "The original sender, {}, has an ID of `{}`.\nThe forwarder, {}, has an ID of `{}`.":
        "El remitente, {}, tiene el ID `{}`.\nEl receptor, {}, tiene el ID `{}`.",
    "{}'s id is `{}`.": "ID {} - `{}`.",
    "Your id is `{}`.": "Tu ID - `{}`.",
    "This group's id is `{}`.": "ID de este grupo - `{}`.",

    "I can't extract a user from this.": "No puedo recuperar el ID de este usuario",
    "<b>User info</b>:": "<b>Información del usuario</b>:",
    "\nFirst Name: {}": "\nNombre: {}",
    "\nLast Name: {}": "\nApellido: {}",
    "\nUsername: @{}": "\nNombre de usuario: @{}",
    "\nPermanent user link: {}": "\nLink permanente del usuario: {}",
    "\n\nThis person is my owner - I would never do anything against them!":
        "\n\nEsta persona es mi dueñ@, nunca haría nada contra él/ella!",
    "\nThis person is one of my sudo users! Nearly as powerful as my owner - so watch it.":
        "\nEsta persona es un@ de mis usuari@s sudo! Casi con tanto poder como mi dueñ@, así que ten cuidado",
    "\nThis person is one of my support users! Not quite a sudo user, but can still gban you off the map.":
        "\nEsta persona es uno de mis usuarios con derechos. No es como un usuario sudo, pero te puede dar global ban, ten cuidado!",
    "\nThis person has been whitelisted! That means I'm not allowed to ban/kick them.":
        "\nEsta persona está en la lista blanca. Esto signidica que no puedo banearla ni echarla.",

    "Its always banhammer time for me!": "Siempre es la hora banhammer para mi!",

    "It's {} in {}": "Está {} en {}",

    "Please reply to a sticker to get its ID.": "Por favor responde a un stciker para obtener su ID.",
    "Please reply to a sticker for me to upload its PNG.": "Por favor, responde a un sticker para que pueda subir su PNG .",

    "Write a location to check the weather.": "Escribe una ubicación para ver que tiempo hace.",
    "I will keep an eye on both happy and sad times!": "Estaré aquí en las buenas y en las malas!",
    "Today in {} is being {}, around {}°C.\n": "Hoy en {} hace {}, alrededor de {}°C.\n",
    "Sorry, location not found.": "Lo siento, ubicación no encontrada.",

    "Deleting identifiable data...": "Borrando datos de usuario...",

    "Try forwarding the following message to me, and you'll see!":
        "Prueba a enviarme el siguiente mensaje y lo verás!",
    "/save test This is a markdown test. _italics_, *bold*, `code`, [URL](example.com) [button](buttonurl:github.com) [button2](buttonurl://google.com:same)":
    """/save test Esto es un test de markdown. _cursiva_, *negrita*, `codigo`, \
[URL](example.com) 
[Botón](buttonurl:github.com)
[Botón2](buttonurl://google.com:same)""",

#Misc GDPR
"send-gdpr": """Tu información personal ha sido borrada.\n\nTen en cuento que esto no te va a desbanear \
de ningún chat, ya que eso son datos de Telegram, NO datos de YanaBot.
Flooding, advertencias, y bans globales también se conservan, a partir de \
[esto](https://ico.org.uk/for-organisations/guide-to-the-general-data-protection-regulation-gdpr/individual-rights/right-to-erasure/), "
que establece claramente que el derecho de cancelación no se aplica \
\"para la realización de una tarea realizada en interés público.\", así como \
el caso de los datos mencionados anteriormente.""",

#Admin
"How am I meant to promote someone that's already an admin?": "¿Como voy a ascender a administrador a alguien que ya lo es?",
"I can't promote myself! Get an admin to do it for me.": "¡No puedo hacerme administradora a mi misma! ¡Avisa a algún administrador para que lo haga!",
"Successfully promoted in *{}*!": " Ascendido a administrador en *{}*!",

"This person CREATED the chat, how would I demote them?": "Esta persona ha creado el chat. ¿Cómo quieres que le quite el admin?",
"Can't demote what wasn't promoted!": "No puedo quitarle el admin si no lo tiene!",
"I can't demote myself!": "No puedo quitarme de ser administradora yo misma!",
"Successfully demoted in *{}*!": "Ya no es administrador en *{}*!",
"Could not demote. I might not be admin, or the admin status was appointed by another user, so I can't act upon them!": 
"No puedo quitarle el admin. Puede que no sea administrador o que el estado de administrador fuese dado por otro usuario, asi que no puedo actuar sobre él!",

"I don't have access to the invite link, try changing my permissions!": "No tengo acceso al link de invitación, prueba cambiando mis permisos!",
"I can only give you invite links for supergroups and channels, sorry!": "Lo siento, solo puedo dar links de invitación para supergrupos y canales.",

"Admins in": "Administradores en",
"this chat": "este chat",
" (Creator)": " (Creador)",

#AFK
"{} is now AFK!": "Ahora {} está ausente!",
"{} is no longer AFK!": "{} ya no está ausente!",
"{} is AFK!": "{} está ausente!",
"{} is AFK! says its because of: \n{}": "{} está ausente! Dice que es porque: \n{}",

#Antiflood
"I like to leave the flooding to natural disasters. But you, you were just a disappointment. Get out.":
     "Suelo tener bastante paciencia con la gente pesada, pero te has pasado. ¡Largo de aquí!",
"I can't kick people here, give me permissions first! Until then, I'll disable antiflood.":
    "No puedo expulsar a la gente aquí, dame permisos primero! Hasta que eso ocurra deshabilitaré el antiflood.",
"Antiflood has been disabled.": "Antiflood ha sido deshabilitado.",
"Antiflood has to be either 0 (disabled), or a number bigger than 3 (enabled)!":
    "Antiflood tiene que ser 0 (deshabilitado), o un número superior a 3 (habilitado)!",
"Antiflood has been updated and set to {}": "Antiflood se ha actualizado y ha sido establecido a {}",
"Unrecognised argument - please use a number, 'off', or 'no'.":
    "Comando desconocido- por favor usa un número, 'off', o 'no'.",
"I'm not currently enforcing flood control!": "Ahora mismo no estoy no controlando el flood!",
"I'm currently banning users if they send more than {} consecutive messages.":
     "Estoy baneando a todos los usuarios que envíen más de {} mensajes consecutivos.",

#Antispam
"I've enabled antispam security in this group. This will help protect you from spammers, unsavoury characters, and the biggest trolls.":
 "He activado la seguridad antispam en este grupo. Esto te ayudará a protegerte contra spammers, personas desagradables y trolls.",

"I've disabled antispam security in this group. GBans wont affect your users anymore. You'll be less protected from any trolls and spammers though!":
    "He desactivado la seguridad antispam en este grupo. Los Bans Globales no afectarán a los usuarios. Estarás menos protegido de trolls y spammers!",

"Give me some arguments to choose a setting! on/off, yes/no!\n\nYour current setting is: {}\nWhen True, any gbans that happen will also happen in your group. When False, they won't, leaving you at the possible mercy of spammers.":
    "Dame algún comando para establecer la configuración! on/off, yes/no!\n\nTu configuración actual es: {}\nCuando sea True, cualquier Ban Global que ocurra tambien ocurrirá en tu grupo. Cuando sea False, los Ban Globales no afectarán en tu grupo, dejandolo a merced de posibles spammers.",

"Globally banned: <b>{}</b>": "Baneado globalmente: <b>{}</b>",
"\nGlobally muted: <b>{}</b>": "\nSilenciado globalmente: <b>{}</b>",
"\nReason: {}": "\nRazón: {}",

#Bans
    "I really wish I could ban admins...": "Ya me gustaría poder banear a administradores...",
    "I'm not gonna BAN myself, are you crazy?": "No voy a banearme a mi misma, ¿estás loco?",
    "Banned!": "¡Baneado!",
    "Well damn, I can't ban that user.": "Vaya, no puedo banear a este usuario!.",
    "You haven't specified a time to ban this user for!": 
        "No has especificado el tiempo para banear a este usuario!",
    "Banned! User will be banned for {}.": "¡Baneado! El usuario ha sido baneado por {}.",

#Blacklist
    "<b>Current blacklisted words in {}:</b>\n": "<b>Palabras en la lista negra en {}:</b>\n",
    "There are no blacklisted messages in <b>{}</b>!": "No hay mensajes en la lista negra en <b>{}</b>!",
    "Added <code>{}</code> to the blacklist in <b>{}</b>!":
        "Añadido <code>{}</code> a la lista negra en <b>{}</b>!",
    "Tell me which words you would like to add to the blacklist.":
        "Dime qué palabras te gustaría añadir a la lista negra.",
    "Removed <code>{}</code> from the blacklist in <b>{}</b>!":
        "Borrado <code>{}</code> de la lista negra en <b>{}</b>!",
    "This isn't a blacklisted trigger...!": "Este no es un comando de la lista negrа...!",
    "None of these triggers exist, so they weren't removed.":
        "Ninguno de estos comandos existía, asi que no han sido borrados.",
    "Removed <code>{}</code> triggers from the blacklist in <b>{}</b>! {} did not exist, so were not removed.":
        "Borrado <code>{}</code> de los comandos de la lista negra en <b>{}</b>! {} no existe, así que no ha sido borrado!.",
    "Tell me which words you would like to remove from the blacklist.":
        "Dime que palabras te gustaría borrat de la lista negra.",

    #Filters
    "*Filters in {}:*\n": "*Filtros en {}:*\n",
    "local filters": "filtros locales",
    "*local filters:*\n": "*filtros locales:*\n",
    "No filters in {}!": "No ha filtros en {}!",
    "There is no note message - You can't JUST have buttons, you need a message to go with it!":
        "No hay mensaje - No puedes tener botones vacíos, necesitas un mensaje que vaya dentro del botón!",
    "You didn't specify what to reply with!": "No has especificado con qué quieres que responda!",
    "Handler '{}' added in *{}*!": "El filtro '{}' ha sido añadido en *{}*!",
    "No filters are active in {}!": "No hay filtros activos en {}!",
    "Yep, I'll stop replying to that in *{}*." : "Valee, dejaré de responder a eso en *{}*.",
    "That's not a current filter - run /filters for all active filters.":
        "Actualmente eso no es un filtro - escribe /filters para ver los filtros activos.",
    
    #Disable
    "Disabled the use of `{}` in *{}*": "Desactivado el uso de `{}` en *{}*",
    "That command can't be disabled": "Ese comando no se puede desactivar!",
    "What should I disable?": "¿Qué debería desactivar?",

    "Enabled the use of `{}` in *{}*": "Activado el uso de `{}` en *{}*",
    "Is that even disabled?": "¿Acaso está desactivado?",
    "What should I enable?": "¿Qué debería activar?",

    "The following commands are toggleable:\n{}": "Los siguientes comandos se pueden desactivar:\n{}",
    "No commands can be disabled.": "No hay comandos que se puedan desactivar.",
    "No commands are disabled in *{}*!": "Bo hay comandos desactivados en *{}*!",
    "No commands are disabled!": "No hay comandos desactivados!",
    "The following commands are currently restricted in *{}*:\n{}":
        "Los siguientes comandos están desactivados en *{}*:\n{}",

#Locks
    "Locked {} messages for all non-admins!": "Bloqueados los mensajes de {}  para todos los no administradores!",
    "What are you trying to lock...? Try /locktypes for the list of lockables":
        "¿Qué estás intentando bloquear...? Escribe /locktypes para ver la lista de los tipos de bloqueos.",
    "I'm not an administrator, or haven't got delete rights.":
        "No soy administrador o no tengo permisos para borrar.",
    "Unlocked {} for everyone!": "Desbloqueado {} para todos!",
    "What are you trying to unlock...? Try /locktypes for the list of lockables":
        "¿Qué estás intentando desbloquear...? Escribe /locktypes para ver la lista de los tipos de bloqueos.",
    "What are you trying to unlock...?": "¿Qué estás intentando desbloquear...?",
    "I see a bot, and I've been told to stop them joining... but I'm not admin!":
        "He visto un bot y se me ha ordenado evitar que entre al grupo..., pero no soy administrador!",
    "Only admins are allowed to add bots to this chat! Get outta here.":
        "¡Solo se permite a los administradores añadir bots! ¡Fuera de aquí!",
    "There are no current locks in *{}*.": "No hay bloqueos en *{}*.",
    "These are the locks in *{}*:": "Estos son los bloqueos en *{}*:",
    "this chat": "este chat",

#Log channel
    "Now, forward the /setlog to the group you want to tie this channel to!":
        "Ahora envia /setlog al grupo con el que quieres vincular este canal!",
    "This channel has been set as the log channel for {}.": 
        "Este canal ha sido configurado como el canal de registro para {}.",
    "Successfully set log channel!": "Canal de registro establecido con éxito!",
    "*The steps to set a log channel are:*\n • add bot to the desired channel\n • send /setlog to the channel\n • forward the /setlog to the group\n":
        """*Los pasos para establecer un canal de registro son:*
 • añade el bot al canal que quieras!)
 • escribe /setlog en el canal
 • envía el /setlog que has puesto en el canal al grupo.""",

    "Channel has been unlinked from {}": "El canal ha sido desvinculado de {}",
    "Log channel has been un-set.": "Canal de registro no establecido.",
    "No log channel has been set yet!": "No hay ningún canal de registro establecido!",

#Users
    "I've seen them in <code>{}</code> chats in total.": 
        "Le he visto en <code>{}</code> chats en total.",
    "I've seen them in... Wow. Are they stalking me? They're in all the same places I am... oh. It's me.":
        "Le he visto en...Wow. ¿Me estás siguiendo? Estás los mismos sitios que yo... oh, pero si soy yo! Que chorprecha!!.",
    
#Msg_deleting
    "Cannot delete all messages. The messages may be too old, I might not have delete rights, or this might not be a supergroup.":
        "No he podido borrar todos los mensajes. Puede que los mensajes sean muy viejos, que no tenga derechos para borrarlos o que esto no sea un supergrupo.",
    "Purge complete.": "Purga completada.",
    "Reply to a message to select where to start purging from.":
        "Responde a un mensaje para seleccionar desde donde empezar la purga.",
    "Whadya want to delete?": "¿Qué quieres borrar?",

#Muting
    "You'll need to either give me a username to mute, or reply to someone to be muted.":
        "Necesitas darme un nombre de usuario para silenciar, o responde a alguien para silenciarle.",
    "I'm not muting myself!": "¡No me voy a silenciar a mi misma!",
    "Afraid I can't stop an admin from talking!": "¡Me temo que no puedo hacer que un administrador pare de hablar!",
    "You'll need to either give me a username to unmute, or reply to someone to be unmuted.":
        "Necesitas darme un nombre de usuario para dejar de silenciarle, o responde a alguien que está silenciado para quitarle el silencio.",
    "This user already has the right to speak in {}.": "Este usuario ya puede hablar en {}.",
    "Yep, {} can start talking again in {}!": "Si, {} puede empezar a hablar otra vez en {}!",
    "This user isn't even in the chat, unmuting them won't make them talk more than they already do!":
        "Este usuario ni siquiera está en el chat.",
    "I really wish I could mute admins...": "Ya me gustaría poder silenciar a administradores...",
    "I'm not gonna MUTE myself, are you crazy?" : "No voy a silenciarme a mi misma, ¿estás loco?",
    "You haven't specified a time to mute this user for!":
        "¡No has especificado el tiempo para silenciar a este usuario!",
    "Muted for {} in {}!": "Silenciado durante {} en {}!",
    "This user is already muted in {}!": "Este usuario ya está silenciado.",
    "Well damn, I can't mute that user.": "Vaya, no puedo silenciar a este usuario.",

    "You'll need to either give me a username to restrict, or reply to someone to be restricted.":
        "Necesitas darme un nombre de usuario para restringir, o responder a alguien para restringirle.",
    "I'm not restricting myself!": "No me voy a restringir a mi misma!",
    "Afraid I can't restrict admins!": "Me temo que no puedo restringir a administradores!",
    "{} is restricted from sending media in {}!": "{} ha sido restringido para enviar media en {}!",
    "This user is already restricted in {}!": "Este usuario ya está restringifo en {}!",
    "This user isn't in the {}!": "Este usuario no está en {}!",

    "You'll need to either give me a username to unrestrict, or reply to someone to be unrestricted.":
        "Necesitas darme un nombre de usuario para quitar la restricción, o responder a un mensaje de esa persona.",
    "This user already has the rights to send anything in {}.": 
        "Este usuario ya tiene permisos para enviar cualquier cosa en {}.",
    "Yep, {} can send media again in {}!": "Si, {} puede volver a enviar media en {}!",
    "This user isn't even in the chat, unrestricting them won't make them send anything than they already do!":
        "ЭEste usuario ni siquiera está en el chat.",
    "I really wish I could restrict admins...": "Ya me gustaría poder restringir a administradores...",
    "I'm not gonna RESTRICT myself, are you crazy?": "No voy a restringirme a mi misma, ¿estás loco?",
    "You haven't specified a time to restrict this user for!": 
        "¡No has especificado el tiempo para restringir a este usuario!",
    "Well damn, I can't restrict that user.": "Vaya, no puedo restringir a este usuario.",
    "{} is muted in {}!": "{} está silenciado en {}!",
    "Restricted from sending media for {} in {}!": "Restringido para enviar media por {} en {}!",
    "Restricted for {} in {}!": "{} Restringido por {} en {}!",

#Notes
    "Get rekt": "¡Te destrozo!.",


#Multi
    "Invalid Chat ID provided!": "El ID del chat no es válido!", #Connections
    "You don't seem to be referring to a user.": "Parece que no te estás refiriendo a ningún usuario.", #Admin, Bans, Muting
    "I can't seem to find this user": "Parece que no puedo encontrar a este usuario.", #Bans, Muting
    "Yes": "Si", #Antispam
    "No": "No", #Antispam

#__main__
    #Module names
        "Admin": "Administrador",
        "AFK": "Ausente (AFK)",
        "AntiFlood": "Antiflood",
        "Bans": "Bans",
        "Word Blacklists": "Lista negra",
        "Filters": "Filtros",
        "Command disabling": "Desactivar comandos",
        "Antispam security": "Seguridad antispam",
        "Locks": "Bloqueos",
        "Log Channels": "Registro de canales",
        "Misc": "Misceláncea",
        "Purges": "Purgas",
        "Muting & Restricting": "Silenciar y Restringir",
        "Notes": "Notas",
        "Reporting": "Reportar",
        "RSS Feed": "Feed RSS",
        "Rules": "Reglas",
        "Connections": "Conexiones",
        "Bios and Abouts": "Biografía",
        "Warnings": "Advertencias",
        "Welcomes/Goodbyes": "Bienvenidas/Despedidas",

#Some main stuff
"Here is the help for the *{}* module:\n{}": "Aquí está la ayuda para el módulo de *{}*:\n{}",
"Back": "Atrás",

"main_start_pm": """Hola, soy * Filterry * \n
* Soy el mejor bot de filtro grupal de Telegram con características especiales *. \n
* Siéntete libre de agregarme a tu chat *. \n
* Pulsa /help para ver mis funciones *. \n
* Desarrollado por @DevelopedBots 💖 *.
""",

    "send-help": """Hola! Mi nombre es * Filterry *. Soy un robot de filtros con muchas funciones específicas. \ n
* Comandos útiles *:
✪ /start: empieza de nuevo
✪ /help: verifique todos los módulos y comandos
✪ /connect (ID de grupo): conecta tu grupo
✪ /source: Verifique los detalles sobre mi fuente
✪ /lang: cambia el idioma del bot.

Si no sabe cómo configurar, consulte * Configuration tutorial *.

Desarrollado por @DevelopedBots 💖
   """,

    "send-group-settings": """Hola! Hay algunas configuraciones disponibles para *{}* - entra y selecciona aquello en lo que
estés interesado.""",

#Misc
"RUNS-K": RUN_STRINGS,
"SLAP_TEMPLATES-K": SLAP_TEMPLATES,
"ITEMS-K": ITEMS,
"HIT-K": HIT,
"THROW-K": THROW,
"ITEMP-K": ITEMS,
"ITEMR-K": ITEMS,
"MARKDOWN_HELP-K": MARKDOWN_HELP,

#GDPR
"send-gdpr": """Tu información personal ha sido borrada.\n\nTen en cuento que esto no te va a desbanear \
de ningún chat, ya que eso son datos de Telegram, NO datos de YanaBot.
Flooding, advertencias, y bans globales también se conservan, a partir de \
[esto](https://ico.org.uk/for-organisations/guide-to-the-general-data-protection-regulation-gdpr/individual-rights/right-to-erasure/), "
que establece claramente que el derecho de cancelación no se aplica \
\"para la realización de una tarea realizada en interés público.\", así como \
el caso de los datos mencionados anteriormente.""",


#Help modules
"Admin_help": """
 - /adminlist | /admins: lista de los administradores de este chat
*Solo administradores:*
 - /pin: Ancla silenciosamente el mensaje respondido: agrega 'loud' o 'notify' para notificar a los usuarios.
 - /unpin: Desancla en mensaje anclado
 - /invitelink: Genera el link de invitación al grupo
 - /promote: Asciende a administrador al usuario al que se le responde
 - /demote: Quita el administrador al usuario al que se le responde
""",

"AFK_help": """
 - /afk <motivo>: Te marca como ausente.
 - brb <motivo>: Hace lo mismo que el comando AFK pero sin ser un comando.
Cuando estás ausente (AFK), cualquier mención será respondida con un mensaje que dice que no estás disponible.
""",

"AntiFlood_help": """
 - /flood: Te muetra el control antiflood actual.
*Solo administradores:*
 - /setflood <int/'no'/'off'>: Activa o desactiva el control de flood
""",

"Antispam security_help": """
*Solo administradores:*
 - /antispam <on/off/yes/no>: Deshabilitará la seguridad antispam en grupo o te dará su configuración actual.
Los propietarios del bot suelen utilizar el antispam para prohibir a los spammers en todos los grupos. Esto ayuda a protegerte \
a ti y a tus grupos mediante la eliminación de los spammers lo más rápido posible. Se pueden desactivar en tu grupo escribiendo  \
/antispam
""",

"Bans_help": """
 - /kickme: Expulsa al usuario que escribe este comando
*Solo administradores:*
 - /ban <userhandle>: banea a un usuario. (via nombre de usuario, o respondiendo a un mensaje suyo)
 - /tban <userhandle> x(m/h/d): banea a un usuario durante x tiempo. (via nombre de usuario, o respondiendo a un mensaje suyo). m = minutos, h = horas, d = días.
 - /unban <userhandle>: desbanea a un usuario. (via nombre de usuario, o respondiendo a un mensaje suyo)
 - /kick <userhandle>: expulsa a un usuario, (via nombre de usuario, o respondiendo a un mensaje suyo)
""",

"Connections_help": """
Acciones disponibles mediante grupos conectados:
 • Ver y editar notas
 • Ver y editar filtros
 • Ver y editar la lista negra
 • Ascender/quitar administrador
 • Ver la lista de administradores, ver link de invitación
 • Desactivar/activar comandos en el chat
 • Silenciar/quitar silencio a usuarios en el chat
 • Restringir/quitar restricción a usuarios en el chat
 • ¡Más en el futuro!
 - /connection <iddelchat>: Conecta al chat remoto
 - /disconnect: Desconecta del chat
 - /allowconnect on/yes/off/no: Permite a los usuarios conectarse al grupo
""",

"Filters_help": """
 - /filters: Lista de todos los filtros en este chat.
*Solo administradores:*
 - /filter <palabraclave> <mensaje con el que responde>: añade un filtro a este chat. El bot responderá a ese mensaje cuando se mencione\
la 'palabraclave'. Si respondes a un sticker con una palabra clave, el bot responderá a la palabra clave con ese sticker. NOTA: todas las palabras \
clave de los filtros están en minúscula. Si quieres que tu palabra clave sea una frase, usa comillas. ej: /filter "hey hola" ¿Qué tal \
te va?
 - /stop <palabraclave>: elimina el filtro.
""",

"Command disabling_help": """
 - /cmds: comprueba el estado actual de los comandos deshabilitados.
*Solo administradores:*
 - /enable <nombre comando>: activa ese comando
 - /disable <nombre comando>: desactiva ese comando
 - /listcmds: lista de todos los comandos que se pueden activar o desactivar
""",

"Locks_help": """
 - /locktypes: lista de todos los tipos de bloqueo posibles
*Solo administradores:*
 - /lock <tipo>: bloquea elementos de un determinado tipo (no disponible en chat privado)
 - /unlock <tipo>: desbloquea elementos de un determinado tipo (no disponible en chat privado)
 - /locks: muestra la lista actual de bloqueos en el chat
Los bloqueos se pueden utilizar para restringir a los usuarios de un grupo.
ej:
Bloquear URL borrará automaticamente todos los mensajes que contengan URLs y que no hayan sido metidos en la lista blanca, bloquear stickers borrará todos los \
stickers, etc.
Bloquear los bots hará que ningun usuario no administrador pueda añadir bots al chat.
""",

"Log Channels_help": """
*Solo administradores:*
- /logchannel: obiene información de registro del canal
- /setlog: configura el canal de registro.
- /unsetlog: elimina el canal de registro.
Para configurar el canal de registro se hace de la siguiente forma:
- añadir el bot al canal deseado (como administrador!)
- escribir /setlog en el canal
- enviar el /setlog en el grupo
""",

"Misc_help": """
 - /id: obtiene la id del grupo. Si se usa respondiendo a un mensaje, obtiene la id de ese usuario.
 - /runs: responde una frase aleatoria de una batería de frases preestablecidas.
 - /slap: abofetea a u usuario, o recibe una bofetada si no lo utilizas como respuesta.
 - /time <lugar>: te da la hora para el lugar indicado.
 - /weather <ciuidad>: muestra el tiempo climatológico para la ciudad indicada.
 - /info: obtiene información de un usuario.
 - /gdpr: borra tu información de la base de datos del bot. Solo en privado.
 - /stickerid: responde a un sticker con esto y te diré la ID del archivo.
 - /getsticker: responde a un sticker con esto y subiré el archivo en PNG.
 - /markdownhelp: resumen rápido de como funciona el markdown en telegram - solo se puede usar en chats privados.
""",

"Purges_help": """
*Solo administradores:*
 - /del: borra el mensaje al que respondes.
 - /purge: borra todos los mensajes que haya desde el final hasta el mensaje al que respondas.
 - /purge <número X>: borra el mensaje al que respondes, y los X mensajes siguientes.
""",

"Muting & Restricting_help": """
*Solo administradores:*
 - /mute <userhandle>: silencia un usuario. Puede ser usado respondiendo a un mensaje, silenciando al usuario al que respondes.
 - /tmute <userhandle> x(m/h/d): silencia a un usuario durante x tiempo.(via nombre de usuario, o respondiendo a un mensaje suyo). m = minutos, h = horas, d = días.
 - /unmute <userhandle>: quita el silencio a un usuario. Puede ser usado como respuesta, quitando el silencio a usuario al que respondes.
 - /restrict <userhandle>: restringe a un usuario para enviar stickers, gif, links o media. Puede ser usado como respuesta, restringiendo al usuario al que respondes.
 - /trestrict <userhandle> x(m/h/d): restringe a un usuario durante x tiempo. (via nombre de usuario, o respondiendo a un mensaje suyo). m = minutos, h = horas, d = días.
 - /unrestrict <userhandle>: quita la restricción a un usuario para enviar stickers, gif, links o media. Puede ser usado como respuesta, quitando la restricción al usuario al que respondes..
""",

"Notes_help": """
 - /get <nombredelanota>: obtienes la nota guardada con este nombre
 - #<nombredelanota>: lo mismo que con /get
 - /notes o /saved: lista de todas las notas guardadas en el chat.
Si quieres recuperar el contenido de una nota sin formato, utiliza `/get <nombredelanota> noformat`. Esto puede \
ser util cuando actualizas una nota, sobre todo si hay botones en ella.
*Solo administradores:*
 - /save <nombredelanota> <contenidodelanota>: guarda 'contenidodelanota' como nota con el nombre 'nombredelanota'
Se puede añadir botones a las notas usando la sintaxis normal de 'markdown' - el link que añadas al boton deberá llevar antes \
`buttonurl:` tal como se muestra aquí: `[textodelbotón](buttonurl:tulink.com)`. Así quedaria configurado un botón en una nota. Mira /markdownhelp para más información.
 - /save <nombredelanota>: guarda el mensaje al que respondes con 'nombredelanota'
 - /clear <nombredelanota>: borra la nota con ese nombre
""",

"Reporting_help":"""
 - /report <motivo>: responde a un mensaje para reportarlo a los administradores.
 - @admin: responde a un mensaje para reportarlo a los administradores.
NOTA: ninguno de estos comandos se activará si es utilizado por los administradores
*Solo administradores*
 - /reports <on/off>: cambia la configuración de los reportes, o te permite ver el estado actual de la configuración.
   - Si se hace en mensaje privado, cambia tu estado
   - Si se hace en un chat, cambia el estado del chat.
""",

"RSS Feed_help": """
 - /addrss <link>: añade un link RSS a las suscripciones.
 - /removerss <link>: quita un link RSS de las suscripciones.
 - /rss <link>: muestra los datos del link y la ultima entrada, sirve sobre todo para hacer tests.
 - /listrss: muestra la lista de los feeds RSS a los que el chat está suscrito.
NOTA: En grupos, solo los administradores pueden añadir/borrar links RSS a las suscripciones del grupo.
""",

"Rules_help": """
 - /rules: te muestra las normas para ese chat
*Solo administradores:*
 - /setrules <tus normas aquí>: configura las reglas de un chat.
 - /clearrules: borra las reglas para el chat en el que estás.
""",

"Sed/Regex_help": """
 - s/<text1>/<text2>(/<flag>): Responde a un mensaje con esto para hacer una operación sed en ese mensaje, cambiando todas \
las cosas de 'text1' con 'text2'. Flags son opcionales, y actualmente incluyen 'i' para ignorar, 'g' para global, \
o nada. Los delimitadores incluyen `/`, `_`, `|`, y `:`. Se admite la agrupación de texto. El mensaje resultante no puede ser \
más largo de {}.
*Recordatorio:* Sed usa algunos caracteres especiales para facilitar la comparación, como estos: `+*.?\\`
Si quieres usar estos caracteres, asegúrate de que no los incluyes!
eg: `\\?`.
""",

"Bios and Abouts_help": """
 - /setbio <texto>: respondiendo a un usuario, guardará su biografía
 - /bio: te mostrará tu biografía o la de otro usuario. 
 - /setme <texto>: te muestra tu información
 - /me: te mostrará tu biografía o la de otro usuario
""",

"Warnings_help": """
 - /warns <userhandle>: te muestra el número de avisos y la razón del usuario al que respondes
 - /warnlist: lista de los filtros de avisos actual.
*Solo administradores:*
 - /warn <userhandle>: advierte a un usuario. Despues de 3 advertencias, el usuario será baneado del grupo. Se puede usar respondiendo a un mensaje.
 - /resetwarn <userhandle>: Resetea las advertencias para un usuario. Puede ser usado como respuesta a un mensaje.
 - /addwarn <palabraclave> <mensaje añadido>: establece un filtro de advertencia en una determinada palabra clave. Si quieres que tu palabra clave \
ser una oración, ponla entre comillas, como aquí: `/addwarn "muy enfadado" Esto es un usuario enfadado`. 
 - /nowarn <palabraclave>: detiene un filtro de advertencia
 - /warnlimit <num>: establece el numero de advertencias
 - /strongwarn <on/yes/off/no>: Si está en on y se excede el numero de advertencias, el usuario será baneado. Si no solo será expulsado
""",

"Welcomes/Goodbyes_help": """
Tus mensajes de Bienvenida/despedida en el grupo se pueden personalizar de múltiples formas. Si quieres que los mensajes sean individualizados \
como mensaje predefinido, sigue estos pasos:
 - `{{first}}`: esto representa el *nombre* del usuario
 - `{{last}}`: esto representa el *apellido* del usuario. Predefinido a *nombre* si el usuario no tiene apellido.
 - `{{fullname}}`: esto representa el nombre *completo*. Por defecto *nombre* del usuario unicamente, si no tiene apellido.
 - `{{username}}`: esto representa el *alias*. Por defecto *meciona* el nombre del usuario si no tiene alias.
 - `{{mention}}`: esto solo *menciona* a un usuario - escribiendo unicamente su nombre.
 - `{{id}}`: esto representa el *id* de usuario.
 - `{{count}}`: esto representa el *numero de miembro*.
 - `{{chatname}}`: esto representa el *nombre del grupo actual*.
Cada variable DEBE ser metida entre `{{}}` para que sea reemplazada.
Los mensajes de bienvenida soportan markdown, asi que puedes hacer que cualquier palabra vaya en negrita/cursiva/monoespaciado/links. \
También puedes poner botones, asi puedes hacer que las bienvenidas queden espectaculares con botones de introducción. \
Para crear un botón que lleve a tus normas, usa esto: `[Normas](buttonurl://t.me/{}?start=group_id)`. \
Simplemente reemplaza el `group_id` con la ID de tu grupo, que puedes obtener via /id, y ya estaría. \
Ten en cuenta que las id de grupo suelen ir precedidas del signo `-`; Ese signo ES NECESARIO, así que por favor \
no lo borres. \
Si tienes el humor suficientes puedes tambien poner imágenes/videos/gif/notas de voz como mensaje de bienvenida,\
respondiendo al mensaje con la imagen/gif/video mediante /setwelcome.
*Solo administradores:*
 - /welcome <on/off>: activa/desactiva los mensajes de bienvenida.
 - /welcome: muestra los ajustes de bienvenida actuales.
 - /welcome noformat: muestra la bienvenida actual, pero sin formato - útil si quieres editar un mensaje de bienvenida!
 - /goodbye -> lo mismo que para /welcome.
 - /setwelcome <alguntexto>: configura tu mensaje de bienvenida. Si se usa respondiendo a media, establece la imagen/gif/video como bienvenida.
 - /setgoodbye <alguntexto>: lo mismo que /setwelcome pero para despedidas.
 - /resetwelcome: resetea el mensaje de bienvenida al mensaje por defecto.
 - /resetgoodbye: resetea el mensaje de despedida al mensaje por defecto.
 - /cleanwelcome <on/off>: Para los nuevos miembros que entran, intenta borrar los mensajes de bienvenida previos, así evita el spam de mensajes de bienvenida en el chat.
 - /cleanservice <on/off/yes/no>: borra los mensajes de servicio; esos mensajes tal que "x se ha unido al grupo" que se ven cuando alguien se une.
 - /welcomesecurity <off/soft/hard>: soft - restringe los permisos del usuario que acaba de entrar, de tal forma que no puede enviar media durante 24 horas, hard - restringe los permisos del usuario para enviar mensages hasta que hace click en el mensaje de \"No soy un bot.\"
"""
}
