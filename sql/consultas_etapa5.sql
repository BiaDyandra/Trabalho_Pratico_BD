-- TRABALHO PRÁTICO - ETAPA 5: CONSULTAS COMPLEXAS
-- Sistema: VetSys

-- 1. Junção entre 4 tabelas (Agendamento, Animal, Tutor, Veterinario)
SELECT a.data_agendamento, a.hora, t.nome, an.nome, v.nome, a.status
FROM Agendamento a
JOIN Animal an ON a.id_Animal = an.id_Animal
JOIN Tutor t ON an.id_Tutor = t.id_Tutor
JOIN Veterinario v ON a.id_Veterinario = v.id_Veterinario
WHERE a.status = 'CONFIRMADO' OR a.status = 'CONCLUIDO';

-- 2. Subconsulta (Animais com peso acima da média da clínica)
SELECT nome, especie, peso 
FROM Animal 
WHERE peso > (SELECT AVG(peso) FROM Animal)
ORDER BY peso DESC;

-- 3. Agregação com GROUP BY (Total de consultas por veterinário)
SELECT v.nome, COUNT(c.id_Consulta) AS total_atendimentos
FROM Veterinario v
JOIN Consulta c ON v.id_Veterinario = c.id_Veterinario
GROUP BY v.nome;

-- 4. Operações de String (LIKE) e Conjunto (IN)
SELECT nome, especie, raca 
FROM Animal 
WHERE especie IN ('Cão', 'Gato') 
AND nome LIKE 'M%';

-- 5. Ordenação e Limitação (Os 5 tratamentos mais recentes)
SELECT t.descricao, t.data_inicio, a.nome AS nome_animal
FROM Tratamento t
JOIN Consulta c ON t.id_Consulta = c.id_Consulta
JOIN Animal a ON c.id_Animal = a.id_Animal
ORDER BY t.data_inicio DESC
LIMIT 5;