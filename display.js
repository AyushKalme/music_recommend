window.addEventListener('load', () => {

    const params = (new URL(document.location)).searchParams;
    const songname = params.get('songname');
    const singer = params.get('singer');
    const emotion = params.get('emotion')

    document.getElementById('display_songname').innerHTML = songname;
    document.getElementById('display_singer').innerHTML = singer;
    document.getElementById('display_emotion').innerHTML = emotion;


})