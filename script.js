 const rankingData = [
            {nome: 'Mestre 1', pontos: 100},
            {nome: 'Mestre 2', pontos: 80},
            {nome: 'Mestre 3', pontos: 70},
            {nome: 'Mestre 4', pontos: 60},
            {nome: 'Mestre 5', pontos: 50},
            {nome: 'Mestre 6', pontos: 40},
            {nome: 'Mestre 7', pontos: 30},
            {nome: 'Mestre 8', pontos: 20},
            {nome: 'Mestre 9', pontos: 10},
            {nome: 'Mestre 10', pontos: 0}
        ];

        const rankingSection = document.getElementById("ranking-section");

        const ul = document.createElement("ol");
        ul.className = "ranking-list";

        rankingData.forEach((mc, index) => {
            const li =document.createElement("li");
            li.className = index === 0 ? "primeiro-lugar" : "";
            li.innerHTML = `
                ${index === 0? '<span class="coroa">👑</span>': ''}
                <span class="mc-name">${mc.nome}</span> - <span class="mc-score">${mc.pontos} pts</span>`;
                ul.appendChild(li);
            
        });

        rankingSection.appendChild(ul);

        
        function toggleInfo(element) {
            element.classList.toggle('active');
        }

        function toggleRanking() {
            const section = document.getElementById("ranking-section");
            section.style.display = section.style.display == "none" || section.style.display === "" ? "block" : "none";
        }