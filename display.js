window.addEventListener('load', () => {

    const params = (new URL(document.location)).searchParams;
    const songname = params.get('songname');
    const singer = params.get('singer');
    const emotion = params.get('emotion')

    document.getElementById('display_songname').innerHTML = songname;
    document.getElementById('display_singer').innerHTML = singer;
    document.getElementById('display_emotion').innerHTML = emotion;


})
















// function WriteToFile(passForm) {
 
//     set fso = CreateObject("Scripting.FileSystemObject"); 
//     set s   = fso.CreateTextFile("<your Path>/filename.txt", True);

//     var firstName = document.getElementById('FirstName');
//     var lastName  = document.getElementById('lastName');

//     s.writeline("First Name :" + FirstName);
//     s.writeline("Last Name :" + lastName);

//     s.writeline("-----------------------------");
//     s.Close();
// }


