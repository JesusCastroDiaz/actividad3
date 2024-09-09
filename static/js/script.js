






function historia(e) {
    const word1 = document.getElementById('word1').value;
    const word2 = document.getElementById('word2').value;
    const word3 = document.getElementById('word3').value;
    const word4 = document.getElementById('word4').value;
    const word5 = document.getElementById('word5').value;
    const word6 = document.getElementById('word6').value;

    if (word1 === "" || word2 === "" || word3 === "" || word4 === "" || word5 === "" || word6 === "") {
        alert("Todos los campos son obligatorios");
        return false;
    }




    const story = `
      Había una vez en un lugar muy lejano en las montañas un arbol llamado ${word1} ${word2}, un arbol grande  y mágico. 
      Cada día saludaba a todos sus amigos de las montañas, ellos le decian por cariño ${word3} y como era un arbol muy diferente, grande alto y adulto  sus ramas y hojas eran de color ${word4}, tenia una mirada muy alegre con sus ojos de color  ${word5}, a este arbol lle gustaba mucho reunirse con sus amigos y hablar de sus experiencias vividas, y ellos se sorprendian. pero tambien le gustaba ${word6}, y disfrutaba hacerlo. 
       `;


    document.getElementById('respuesta').innerText = story;
}






