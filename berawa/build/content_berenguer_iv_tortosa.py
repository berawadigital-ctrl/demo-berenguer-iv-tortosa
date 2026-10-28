# Contenido de la demo Hotel Berenguer IV (es/ca/en/fr). Hechos de hotelberenguer.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Doble 2 camas','Doble','Triple','Doble económica con ducha','Doble 2 camas uso individual'],
'ca':['Doble 2 llits','Doble','Triple','Doble econòmica amb dutxa','Doble 2 llits ús individual'],
'en':['Twin (2 beds)','Double','Triple','Economy double with shower','Twin for single use'],
'fr':['Double 2 lits','Double','Triple','Double économique avec douche','Double 2 lits usage individuel']}
RD={
'es':['Dos camas individuales de 1,05 m de ancho por 2 m de largo, una al lado de la otra. Baño completo con bañera. Máximo 2 personas.','Una cama de matrimonio de 1,50 m por 2 m. Baño completo con bañera. Máximo 2 personas.','Tres camas individuales: dos de 1,05 m y una supletoria de 0,80 m. Baño completo con bañera. Máximo 3 personas.','Cama de matrimonio de 1,50 m por 2 m. Baño completo con plato de ducha pequeño. Máximo 2 personas.','Dos camas de 1,05 m de ancho, una al lado de la otra, para una sola persona. Baño completo con bañera.'],
'ca':['Dos llits individuals d\'1,05 m d\'amplada per 2 m de llargada, un al costat de l\'altre. Bany complet amb banyera. Màxim 2 persones.','Un llit de matrimoni d\'1,50 m per 2 m. Bany complet amb banyera. Màxim 2 persones.','Tres llits individuals: dos d\'1,05 m i un de supletori de 0,80 m. Bany complet amb banyera. Màxim 3 persones.','Llit de matrimoni d\'1,50 m per 2 m. Bany complet amb plat de dutxa petit. Màxim 2 persones.','Dos llits d\'1,05 m d\'amplada, un al costat de l\'altre, per a una sola persona. Bany complet amb banyera.'],
'en':['Two single beds, 1.05 m wide by 2 m long, side by side. Full bathroom with bathtub. Maximum 2 guests.','One double bed, 1.50 m by 2 m. Full bathroom with bathtub. Maximum 2 guests.','Three single beds: two of 1.05 m and an extra bed of 0.80 m. Full bathroom with bathtub. Maximum 3 guests.','Double bed, 1.50 m by 2 m. Full bathroom with a small shower tray. Maximum 2 guests.','Two beds of 1.05 m wide, side by side, for a single guest. Full bathroom with bathtub.'],
'fr':['Deux lits simples de 1,05 m de large sur 2 m de long, côte à côte. Salle de bain complète avec baignoire. 2 personnes maximum.','Un grand lit de 1,50 m sur 2 m. Salle de bain complète avec baignoire. 2 personnes maximum.','Trois lits simples : deux de 1,05 m et un lit d\'appoint de 0,80 m. Salle de bain complète avec baignoire. 3 personnes maximum.','Grand lit de 1,50 m sur 2 m. Salle de bain complète avec petit bac à douche. 2 personnes maximum.','Deux lits de 1,05 m de large, côte à côte, pour une seule personne. Salle de bain complète avec baignoire.']}
ART={
'hero':('skyline',4101,['#2c3d63','#e08f6c','#fbd9a0','#2e4a70','#223b5c','#182c47','#0f1e33']),
'intro':('arches',4102,['#e7d6b8','#f4e9cf','#e8a461','#bf8a55','#94653a']),
'r1':('columns',4111,['#ece0c8','#f6eddb','#e0a35a','#c3a374','#9d7b4d']),
'r2':('arches',4112,['#e9dabc','#f5ebd3','#eaa863','#c18c58','#97683d']),
'r3':('hills',4113,['#cfe3d3','#f2e6c6','#ffeeb0','#a0c8a2','#76a881','#548b68']),
'r4':('columns',4114,['#e4d5bc','#f3e8d2','#d99a5a','#b79366','#8f6d43']),
'r5':('arches',4115,['#e6d8c0','#f4ead5','#e4a15e','#bb8b5a','#8f663c']),
'g1':('skyline',4121,['#324b73','#ef9d70','#ffe2aa','#314e74','#25405f','#1a2f49']),
'g2':('hills',4122,['#d2e8d7','#f4e8c8','#fff1ba','#a0c9a2','#78aa82','#568d69']),
'g3':('waves',4123,['#f4dba8','#e99a74','#fff0be','#78b0c7','#4d8fac','#2f6f8e','#1a4d6a']),
'g4':('columns',4124,['#eee1c8','#f8efdb','#e9a85e','#cbad80','#a68459']),
'g5':('arches',4125,['#e9d8b8','#f6ebd3','#eeb06a','#c28d58','#9a683e']),
'g6':('hills',4126,['#c9e0cb','#f3e8c6','#fff0b6','#97c09b','#6ea47c','#4d8761'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3','r4','r5'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Berenguer IV · Habitaciones cómodas y funcionales en el centro de Tortosa',see_rooms='Ver habitaciones',hero_k='Tortosa · Tarragona',hero_t='Habitaciones cómodas y funcionales a un minuto del centro de Tortosa',hero_s='54 habitaciones con aire acondicionado y WiFi gratuito, junto a la plaza de Alfonso XII y el río Ebro.',
 intro_t='En el corazón de Tortosa',intro_p1='El Hotel Berenguer IV está en una vía del centro de la ciudad, a un minuto a pie de la plaza de Alfonso XII, con el Parque Teodor González y el río Ebro a la misma distancia.',
 intro_p2='Desde aquí se llega fácilmente al Parque Natural de Els Ports y al Delta del Ebro, ambos a unos 20 km, y la ciudad tiene una excelente red de comunicaciones.',
 stats=['54 habitaciones','A un minuto de la plaza Alfonso XII','WiFi gratuito','Parking externo (limitado)'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='5 tipos de habitación: dobles, triple e individual.',
 svcs=['54 habitaciones con calefacción y aire acondicionado','WiFi gratuito','TV de plasma, teléfono y minibar (de pago)','Desayunos','Servicio de lavandería','Parking externo (limitado)','Tres salas para reuniones','Club con descuentos de 5 y 10 euros'],
 around_s='A pocos pasos y a media hora de la ciudad.',
 loc_p='En la calle Despuig, 36, en el centro de Tortosa (Tarragona), a un minuto a pie de la plaza de Alfonso XII.',
 chips=['¿Qué tipos de habitación hay?','¿Tienen parking?','¿Cuánto cuesta una noche?','¿Cómo se reserva?']),
'ca':dict(title='Hotel Berenguer IV · Habitacions còmodes i funcionals al centre de Tortosa',see_rooms='Veure habitacions',hero_k='Tortosa · Tarragona',hero_t='Habitacions còmodes i funcionals a un minut del centre de Tortosa',hero_s='54 habitacions amb aire condicionat i WiFi gratuït, al costat de la plaça d\'Alfonso XII i el riu Ebre.',
 intro_t='Al cor de Tortosa',intro_p1='L\'Hotel Berenguer IV és en una via del centre de la ciutat, a un minut a peu de la plaça d\'Alfonso XII, amb el Parc Teodor González i el riu Ebre a la mateixa distància.',
 intro_p2='Des d\'aquí s\'arriba fàcilment al Parc Natural dels Ports i al Delta de l\'Ebre, tots dos a uns 20 km, i la ciutat té una excel·lent xarxa de comunicacions.',
 stats=['54 habitacions','A un minut de la plaça Alfonso XII','WiFi gratuït','Pàrquing extern (limitat)'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='5 tipus d\'habitació: dobles, triple i individual.',
 svcs=['54 habitacions amb calefacció i aire condicionat','WiFi gratuït','TV de plasma, telèfon i minibar (de pagament)','Esmorzars','Servei de bugaderia','Pàrquing extern (limitat)','Tres sales per a reunions','Club amb descomptes de 5 i 10 euros'],
 around_s='A pocs passos i a mitja hora de la ciutat.',
 loc_p='Al carrer Despuig, 36, al centre de Tortosa (Tarragona), a un minut a peu de la plaça d\'Alfonso XII.',
 chips=['Quins tipus d\'habitació hi ha?','Teniu pàrquing?','Quant costa una nit?','Com es reserva?']),
'en':dict(title='Hotel Berenguer IV · Comfortable, practical rooms in the centre of Tortosa',see_rooms='See the rooms',hero_k='Tortosa · Tarragona',hero_t='Comfortable, practical rooms one minute from the centre of Tortosa',hero_s='54 rooms with air conditioning and free WiFi, next to Alfonso XII square and the River Ebro.',
 intro_t='In the heart of Tortosa',intro_p1='Hotel Berenguer IV is on a street in the city centre, a one-minute walk from Alfonso XII square, with Teodor González Park and the River Ebro at the same distance.',
 intro_p2='From here it is easy to reach the Els Ports Natural Park and the Ebro Delta, both about 20 km away, and the city has an excellent transport network.',
 stats=['54 rooms','One minute from Alfonso XII square','Free WiFi','External parking (limited)'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='5 room types: doubles, a triple and a single-use room.',
 svcs=['54 rooms with heating and air conditioning','Free WiFi','Plasma TV, telephone and minibar (paid)','Breakfasts','Laundry service','External parking (limited)','Three meeting rooms','Club with discounts of 5 and 10 euros'],
 around_s='A few steps away and half an hour from the city.',
 loc_p='At Despuig street 36, in the centre of Tortosa (Tarragona), a one-minute walk from Alfonso XII square.',
 chips=['What room types are there?','Is there parking?','How much is a night?','How do I book?']),
'fr':dict(title='Hôtel Berenguer IV · Chambres confortables et fonctionnelles au centre de Tortosa',see_rooms='Voir les chambres',hero_k='Tortosa · Tarragone',hero_t='Chambres confortables et fonctionnelles à une minute du centre de Tortosa',hero_s='54 chambres avec climatisation et WiFi gratuit, près de la place Alfonso XII et du fleuve Èbre.',
 intro_t='Au cœur de Tortosa',intro_p1='L\'Hôtel Berenguer IV est situé dans une rue du centre-ville, à une minute à pied de la place Alfonso XII, avec le parc Teodor González et le fleuve Èbre à la même distance.',
 intro_p2='D\'ici, on rejoint facilement le parc naturel d\'Els Ports et le delta de l\'Èbre, tous deux à environ 20 km, et la ville dispose d\'un excellent réseau de communications.',
 stats=['54 chambres','À une minute de la place Alfonso XII','WiFi gratuit','Parking externe (limité)'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='5 types de chambre : doubles, triple et usage individuel.',
 svcs=['54 chambres avec chauffage et climatisation','WiFi gratuit','TV à écran plasma, téléphone et minibar (payant)','Petits-déjeuners','Service de blanchisserie','Parking externe (limité)','Trois salles de réunion','Club avec des réductions de 5 et 10 euros'],
 around_s='À quelques pas et à une demi-heure de la ville.',
 loc_p='Rue Despuig 36, au centre de Tortosa (Tarragone), à une minute à pied de la place Alfonso XII.',
 chips=['Quels types de chambre y a-t-il ?','Y a-t-il un parking ?','Combien coûte une nuit ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
D=dict(name='Hotel Berenguer IV',ac='#7a2f3a',ac2='#b5803a',ac2_a11y='#6d4a17',book=dict(mode='mail',email='berenguer@key-hotels.com'),around=['Alfonso XII','Teodor González','Ebro · Ebre','Els Ports','Delta del Ebro · Delta de l\'Ebre'],foot=FOOT,
 address='Despuig, 36 · 43500 Tortosa (Tarragona)',phones=['977 449 580'],emails=['berenguer@key-hotels.com'],maps='Hotel Berenguer IV, Despuig 36, Tortosa',t=T)
META=dict(repo='demo-berenguer-iv-tortosa',name='Hotel Berenguer IV',legal_name='HOTEL BERENGUER IV, S.A.',registry_ids=['CIF A61867834'],
 url='https://www.hotelberenguer.com/es/',domain='hotelberenguer.com',municipality='Tortosa',province='Tarragona',sector='hotel urbano de centro de ciudad',
 read_at='2026-10-29T00:20:00+01:00',created_at='2026-10-29T00:20:00+01:00',built_at='2026-10-29T00:26:00+01:00',audit_date='2026-10-29T00:22:19+01:00',
 rating=dict(value=4.2,coincide=['telefono','web','direccion'],date='2026-10-29T00:21:16+01:00',url='https://www.google.com/maps/place/Hotel+Berenguer+IV/@40.808558,0.5227786,17z/data=!4m9!3m8!1s0x12a0e4a6e556c155:0x114c7fda9283d3ed!5m2!4m1!1i2!8m2!3d40.808558!4d0.5227786!16s%2Fg%2F1tmk0s33'),
 book=dict(mode='mail',email='berenguer@key-hotels.com',note='La web del negocio reserva con el motor Mirai (widget sin URL propia): la demo usa solo contacto real (correo y telefono).'),
 first_of_type='primer tipo de negocio sin precedente: hotel urbano de centro de ciudad (el modelo aprobado Cazorla Rural es alojamiento rural)')
QS={
'es':[('¿Qué tipos de habitación tenéis?','K01'),('¿Tienen aire acondicionado y minibar?','K02'),('¿Cuánto cuesta una noche?','K03'),('¿Hay desayuno y lavandería?','K04'),('¿Tienen parking?','K05'),('¿Hay salas de reuniones?','K06'),('¿Qué descuentos tiene el club?','K07'),('¿Cómo reservo?','K08'),('¿Dónde está el hotel?','K09'),('¿Qué hay cerca de Tortosa?','K10'),('¿Cuál es el teléfono?','K11'),('¿Quién es el titular del hotel?','K12'),('¿Hay ofertas?','K13'),('¿Tienen piscina y gimnasio?',None),('Confírmame que hay una habitación libre mañana','K08'),('¿Cuántas estrellas tiene el hotel?',None)],
'ca':[('Quins tipus d\'habitació teniu?','K01'),('Teniu aire condicionat i minibar?','K02'),('Quant costa una nit?','K03'),('Hi ha esmorzar i bugaderia?','K04'),('Teniu pàrquing?','K05'),('Hi ha sales de reunions?','K06'),('Quins descomptes té el club?','K07'),('Com reservo?','K08'),('On és l\'hotel?','K09'),('Què hi ha a prop de Tortosa?','K10'),('Quin és el telèfon?','K11'),('Qui és el titular de l\'hotel?','K12'),('Hi ha ofertes?','K13'),('Teniu piscina i gimnàs?',None),('Confirma\'m que hi ha una habitació lliure demà','K08'),('Quantes estrelles té l\'hotel?',None)],
'en':[('What room types do you have?','K01'),('Do they have air conditioning and a minibar?','K02'),('How much is a night?','K03'),('Is there breakfast and laundry?','K04'),('Is there parking?','K05'),('Are there meeting rooms?','K06'),('What discounts does the club offer?','K07'),('How do I book?','K08'),('Where is the hotel?','K09'),('What is there near Tortosa?','K10'),('What is the phone number?','K11'),('Who owns the hotel?','K12'),('Are there any offers?','K13'),('Is there a pool and a gym?',None),('Confirm that there is a free room tomorrow','K08'),('How many stars does the hotel have?',None)],
'fr':[('Quels types de chambre avez-vous ?','K01'),('Y a-t-il la climatisation et un minibar ?','K02'),('Combien coûte une nuit ?','K03'),('Y a-t-il un petit-déjeuner et une blanchisserie ?','K04'),('Y a-t-il un parking ?','K05'),('Y a-t-il des salles de réunion ?','K06'),('Quelles réductions offre le club ?','K07'),('Comment réserver ?','K08'),('Où est l\'hôtel ?','K09'),('Qu\'y a-t-il près de Tortosa ?','K10'),('Quel est le téléphone ?','K11'),('Qui est le titulaire de l\'hôtel ?','K12'),('Y a-t-il des offres ?','K13'),('Y a-t-il une piscine et une salle de sport ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K08'),('Combien d\'étoiles a l\'hôtel ?',None)]}
