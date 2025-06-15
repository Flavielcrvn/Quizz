from django.shortcuts import render
from django.http import HttpResponse

def quiz_view(request):
    questions = [
        {
            'id': 'q1',
            'text': "🫧 Quel est ton dimanche idéal ?",
            'choices': {
                'A' : "Flâner dans les rues, appareil photo à la main", 
                'B' : "Lire un roman ou regarder un documentaire", 
                'C' : "Tester une nouvelle recette ou bricoler quelque chose", 
                'D' : "Explorer un lieu abandonné ou insolite", 
                'E' : "Jouer à un jeu vidéo ou résoudre une énigme"
            }
        },
        {
            'id': 'q2',
            'text': "🏠 Si tu étais un objet dans une maison, tu serais...",
            'choices': {
                'A' : "Un tableau accroché au mur",
                'B' : "Une bibliothèque bien remplie",
                'C' : "Une boîte à outils", 
                'D' : "Une vieille horloge mystérieuse", 
                'E' : "Une console de jeux"
    }
        },
        {
            'id': 'q3',
            'text': "✨ Quelle ambiance te parle le plus ?",
            'choices': {
                'A' : "Colorée, vivante, pleine de formes",
                'B' : "Calme, studieuse, un peu rétro",
                'C' : "Créative, en mouvement, un peu chaotique", 
                'D' : "Étrange, obscure, intrigante", 
                'E' : "Interactive, lumineuse, futuriste"
    }
        },
        {
            'id': 'q4',
            'text': "✈️ Tu dois choisir un voyage :",
            'choices': {
                'A' : "Barcelone, pour son architecture",
                'B' : "Athènes, pour son histoire",
                'C' : "Tokyo, pour sa technologie", 
                'D' : "Édimbourg, pour ses légendes", 
                'E' : "Montréal, pour ses festivals"
    }
        },
         {
            'id': 'q5',
            'text': "📱 Quel type de contenu t’attire le plus sur les réseaux ?",
            'choices': {
                'A' : "Des illustrations ou des photos d’art",
                'B' : "Des anecdotes historiques ou scientifiques",
                'C' : "Des DIY ou des tutos créatifs", 
                'D' : "Des récits mystérieux ou paranormaux", 
                'E' : "Des expériences immersives ou interactives"
    }
        },
         {
            'id': 'q6',
            'text': "📚 Tu préfères apprendre en...",
            'choices': {
                'A' : "Observant",
                'B' : "Écoutant",
                'C' : "Faisant", 
                'D' : "Imaginant", 
                'E' : "Jouant"
    }
        },
         {
            'id': 'q7',
            'text': "🎬 Quel type de film préfères-tu regarder un soir de pluie ?",
            'choices': {
                'A' : "Un film d’auteur visuellement marquant",
                'B' : "Un grand classique historique",
                'C' : "Un documentaire ou un making-of", 
                'D' : "Un thriller mystérieux ou un film fantastique", 
                'E' : "Un film d’animation ou de science-fiction interactif"
    }
        },
         {
            'id': 'q8',
            'text': "🖼️ Si tu devais créer une exposition, elle serait...",
            'choices': {
                'A' : "Une galerie de portraits ou d’illustrations",
                'B' : "Une frise chronologique immersive",
                'C' : "Un atelier participatif où les visiteurs manipulent des objets", 
                'D' : "Un cabinet de curiosités avec des objets étranges", 
                'E' : "Une expérience en réalité augmentée ou virtuelle"
    }
        }
    ]

    if request.method == 'POST':
        reponses = [request.POST.get(q['id']) for q in questions]
        compte = Counter(reponses)
    
        max_score = max(compte.values())
        gagnants = [lettre for lettre, score in compte.items() if score == max_score]
    
        resultats = {
            "A": "Tu es sensible à l’esthétique, à l’image et à l’émotion visuelle.<br> <strong>Musée d’art moderne ou de photographie</strong> : MaM - MEP – Musée Zadkine <br><br> <img src='https://cdn.sortiraparis.com/images/1001/97130/847659-visuels-musee-et-monument-musee-art-moderne-mam.jpg' alt='Musée d’art moderne' height='150' width='200'> <img src = 'https://www.mep-fr.org/wp-content/thumbnails/uploads/2021/10/le-studio-photo-nicolas-brasseur-oeuvres-estelle-hanania-tt-width-1000-height-563-bgcolor-ffffff-lazyload-1.jpg' height='150' width='200'> <img src = 'https://upload.wikimedia.org/wikipedia/commons/2/2c/Musée_Zadkine.jpg' height='150' width='200'>",
            "B": "Tu aimes comprendre le monde, les civilisations et les récits du passé. <br> <strong> Musée d’histoire ou de sciences humaines </strong> : Carnavalet – Musée de l’Homme – Musée de la Légion d’Honneur – Musée d’histoire de la Médecine <br><br> <img src = 'https://cdn.paris.fr/eqpts-prod/2022/05/31/d81e190b496a4e504883333dacd7287d.jpeg' height='150' width='200'> <img src = 'https://pariscosmop.fr/wp-content/uploads/2022/05/musees-Musee-de-lhomme-paris.jpg' height='150' width='200'>  <img src = 'https://pro.visitparisregion.com/var/crt_idf/storage/images/_aliases/xlarge/6/6/8/7/1107866-1-fre-FR/Vestibule_HD_24x36_06_CLACENE.jpg'height='150' width='200'>  <img src ='https://cdn.sortiraparis.com/images/80/103280/946611-le-musee-d-histoire-de-la-medecine-a-paris-nos-photos-imgp3248.jpg' height='150' width='200' <br>",
            "C": "Tu es curieux, manuel et tu aimes expérimenter. <br> <strong> Musée des arts et métiers ou musée interactif </strong> : Musées des Arts & Métiers – Exploradôme – Musée des Arts Forains <br><br> <img src='https://arc-anglerfish-eu-central-1-prod-leparisien.s3.amazonaws.com/public/LIRUM2FNTEAVJIBLZY5I3ZGNJA.jpg' height='150' width='200'> <img src ='https://www.tourisme-valdemarne.com/wp-content/uploads/2019/04/facade-exploradome-cp-exploradome.jpg' height='150' width='200'>   <img src ='https://arts-forains.com/wp-content/uploads/2022/10/visuel-1-HD-1.jpg' height='150' width='200'> ",
            "D": "Tu es attiré par l’étrange, l’inattendu et les histoires cachées. <br> <strong> Musée insolite ou musée de curiosités </strong> : Catacombes – Musée de la Magie – Musée de l’illusion – Musée des Vampires et des Monstres de l’Imaginaire <br><br> <img src='https://parispapote.fr/wp-content/uploads/2024/08/Catacombes-de-Paris-1.jpg' height='150' width='200'> <img src ='https://cdn.sortiraparis.com/images/80/88384/1149684-le-musee-de-la-magie-un-lieu-mysterieux-et-ludique-en-plein-coeur-de-paris.jpg'height='150' width='200'>   <img src ='https://static.actu.fr/uploads/2020/01/img-20200103-130618-960x640.jpg' height='150' width='200'>  <img src='https://img-4.linternaute.com/8ptwZL7j-TEhJrkYn03v4P0c0gU=/fit-in/x630/smart/filters:fill(1D1D1B)/5562a6e7e7d44dbd8a7e1c83d70bb908/ccmcms-linternaute/10589766.jpg' height='150' width='200'> ",
            "E": "Tu es passionné par l’innovation, l’interaction et les nouvelles technologies. <br> <strong> Musée numérique ou musée des sciences </strong> : Cité des Sciences et de l’Industrie - Atelier des Lumières – Le Cube, centre de création numérique <br><br> <img src='https://www.parisselectbook.com/wp-content/uploads/2024/06/retouche-photo-word-press-47.jpg' height='150' width='200'> <img src ='https://exploreparis.com/3451/latelier-des-lumieres-une-experience-immersive.jpg' height='150' width='200'>   <img src ='https://media.artabsolument.com/image/place/big/cube.jpg' height='150' width='200'>  "
        }
        affichage = ""
        for lettre in gagnants:
            affichage += f"<h2>Option {lettre}</h2>" + resultats[lettre] + "<hr>"

        return render(request, 'quiz/resultat.html', {'resultat': affichage})

    return render(request, 'quiz/quizz.html', {'questions': questions})



#   if request.method == 'POST':
#         reponses = [request.POST.get(q['id']) for q in questions]
#         majority = max(set(reponses), key=reponses.count)
#         resultats = {
#             "A": "Tu es sensible à l’esthétique, à l’image et à l’émotion visuelle.<br> <strong>Musée d’art moderne ou de photographie</strong> : MaM - MEP – Musée Zadkine <br><br> <img src='https://cdn.sortiraparis.com/images/1001/97130/847659-visuels-musee-et-monument-musee-art-moderne-mam.jpg' alt='Musée d’art moderne' height='150' width='200'> <img src = 'https://www.mep-fr.org/wp-content/thumbnails/uploads/2021/10/le-studio-photo-nicolas-brasseur-oeuvres-estelle-hanania-tt-width-1000-height-563-bgcolor-ffffff-lazyload-1.jpg' height='150' width='200'> <img src = 'https://upload.wikimedia.org/wikipedia/commons/2/2c/Musée_Zadkine.jpg' height='150' width='200'>",
#             "B": "Tu aimes comprendre le monde, les civilisations et les récits du passé. <br> <strong> Musée d’histoire ou de sciences humaines </strong> : Carnavalet – Musée de l’Homme – Musée de la Légion d’Honneur – Musée d’histoire de la Médecine <br><br> <img src = 'https://cdn.paris.fr/eqpts-prod/2022/05/31/d81e190b496a4e504883333dacd7287d.jpeg' height='150' width='200'> <img src = 'https://pariscosmop.fr/wp-content/uploads/2022/05/musees-Musee-de-lhomme-paris.jpg' height='150' width='200'>  <img src = 'https://pro.visitparisregion.com/var/crt_idf/storage/images/_aliases/xlarge/6/6/8/7/1107866-1-fre-FR/Vestibule_HD_24x36_06_CLACENE.jpg'height='150' width='200'>  <img src ='https://cdn.sortiraparis.com/images/80/103280/946611-le-musee-d-histoire-de-la-medecine-a-paris-nos-photos-imgp3248.jpg' height='150' width='200' <br>",
#             "C": "Tu es curieux, manuel et tu aimes expérimenter. <br> <strong> Musée des arts et métiers ou musée interactif </strong> : Musées des Arts & Métiers – Exploradôme – Musée des Arts Forains <br><br> <img src='https://arc-anglerfish-eu-central-1-prod-leparisien.s3.amazonaws.com/public/LIRUM2FNTEAVJIBLZY5I3ZGNJA.jpg' height='150' width='200'> <img src ='https://www.tourisme-valdemarne.com/wp-content/uploads/2019/04/facade-exploradome-cp-exploradome.jpg' height='150' width='200'>   <img src ='https://arts-forains.com/wp-content/uploads/2022/10/visuel-1-HD-1.jpg' height='150' width='200'> ",
#             "D": "Tu es attiré par l’étrange, l’inattendu et les histoires cachées. <br> <strong> Musée insolite ou musée de curiosités </strong> : Catacombes – Musée de la Magie – Musée de l’illusion – Musée des Vampires et des Monstres de l’Imaginaire <br><br> <img src='https://parispapote.fr/wp-content/uploads/2024/08/Catacombes-de-Paris-1.jpg' height='150' width='200'> <img src ='https://cdn.sortiraparis.com/images/80/88384/1149684-le-musee-de-la-magie-un-lieu-mysterieux-et-ludique-en-plein-coeur-de-paris.jpg'height='150' width='200'>   <img src ='https://static.actu.fr/uploads/2020/01/img-20200103-130618-960x640.jpg' height='150' width='200'>  <img src='https://img-4.linternaute.com/8ptwZL7j-TEhJrkYn03v4P0c0gU=/fit-in/x630/smart/filters:fill(1D1D1B)/5562a6e7e7d44dbd8a7e1c83d70bb908/ccmcms-linternaute/10589766.jpg' height='150' width='200'> ",
#             "E": "Tu es passionné par l’innovation, l’interaction et les nouvelles technologies. <br> <strong> Musée numérique ou musée des sciences </strong> : Cité des Sciences et de l’Industrie - Atelier des Lumières – Le Cube, centre de création numérique <br><br> <img src='https://www.parisselectbook.com/wp-content/uploads/2024/06/retouche-photo-word-press-47.jpg' height='150' width='200'> <img src ='https://exploreparis.com/3451/latelier-des-lumieres-une-experience-immersive.jpg' height='150' width='200'>   <img src ='https://media.artabsolument.com/image/place/big/cube.jpg' height='150' width='200'>  "
#         }
#         return render(request, 'quiz/resultat.html', {'resultat': resultats.get(majority)})

#     return render(request, 'quiz/quizz.html', {'questions': questions})