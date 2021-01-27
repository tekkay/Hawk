import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')

for voice in voices:
    if voice.name == 'brazil':
        engine.setProperty('voice', voice.id)

engine.say('Como parte do nosso objetivo de acelerar o processo de fazer negócios, ajudamos nossos clientes a adicionar novos documentos ao DocuSign para serem assinados e coletar informações. Em geral, eles "marcariam" manualmente esses documentos para indicar onde as pessoas devem preencher e assinar. Utilizando a extração de entidade personalizada do AutoML Natural Language, podemos usar grandes conjuntos de dados para treinar nosso modelo e melhorar continuamente o processo, independentemente da origem do documento.')
engine.runAndWait()
