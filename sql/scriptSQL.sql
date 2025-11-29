-- 1. LIMPEZA (Garante que começamos do zero)
DROP DATABASE IF EXISTS clinica_vet_db;

-- 2. CRIAÇÃO DO BANCO
CREATE DATABASE clinica_vet_db;
USE clinica_vet_db;

-- 3. CRIAÇÃO DAS TABELAS
CREATE TABLE Tutor (
    id_Tutor INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20),
    email VARCHAR(100),
    endereco VARCHAR(255)
);

CREATE TABLE Veterinario (
    id_Veterinario INT AUTO_INCREMENT PRIMARY KEY,
    CRMA VARCHAR(20) UNIQUE NOT NULL,
    nome VARCHAR(100) NOT NULL,
    especialidade VARCHAR(50),
    telefone VARCHAR(20)
);

CREATE TABLE Animal (
    id_Animal INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(45) NOT NULL,
    especie VARCHAR(45) NOT NULL,
    raca VARCHAR(45),
    data_nascimento DATE,
    peso DECIMAL(5,2),
    porte VARCHAR(45),
    sexo VARCHAR(45),
    castrado ENUM('SIM', 'NÃO') NOT NULL,
    id_Tutor INT NOT NULL,
    FOREIGN KEY (id_Tutor) REFERENCES Tutor(id_Tutor)
);

CREATE TABLE Agendamento (
    id_Agendamento INT AUTO_INCREMENT PRIMARY KEY,
    data_agendamento DATE NOT NULL,
    hora TIME NOT NULL,
    status ENUM('PENDENTE', 'CONFIRMADO', 'CANCELADO', 'CONCLUIDO') DEFAULT 'PENDENTE',
    id_Veterinario INT NOT NULL,
    id_Animal INT NOT NULL,
    FOREIGN KEY (id_Veterinario) REFERENCES Veterinario(id_Veterinario),
    FOREIGN KEY (id_Animal) REFERENCES Animal(id_Animal)
);

CREATE TABLE Consulta (
    id_Consulta INT AUTO_INCREMENT PRIMARY KEY,
    data_consulta DATE NOT NULL,
    sintomas VARCHAR(100),
    diagnostico VARCHAR(200),
    id_Veterinario INT NOT NULL,
    id_Animal INT NOT NULL,
    FOREIGN KEY (id_Veterinario) REFERENCES Veterinario(id_Veterinario),
    FOREIGN KEY (id_Animal) REFERENCES Animal(id_Animal)
);

CREATE TABLE Tratamento (
    id_Tratamento INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(255),
    data_inicio DATE,
    data_fim_previsto DATE,
    id_Consulta INT NOT NULL,
    FOREIGN KEY (id_Consulta) REFERENCES Consulta(id_Consulta)
);

-- 4. POVOAMENTO DO BANCO DE DADOS (INSERTS)

-- Inserindo Tutores
INSERT INTO Tutor (nome, telefone, email, endereco) VALUES
('João Silva', '(11) 99999-0001', 'joao@email.com', 'Rua A, 100'),
('Maria Oliveira', '(11) 99999-0002', 'maria@email.com', 'Rua B, 200'),
('Carlos Souza', '(11) 99999-0003', 'carlos@email.com', 'Av Paulista, 1500'),
('Ana Costa', '(21) 98888-0004', 'ana@email.com', 'Rua das Flores, 30'),
('Pedro Santos', '(31) 97777-0005', 'pedro@email.com', 'Rua do Lago, 5'),
('Lucia Lima', '(41) 96666-0006', 'lucia@email.com', 'Av Brasil, 500'),
('Roberto Dias', '(51) 95555-0007', 'roberto@email.com', 'Rua X, 10'),
('Fernanda Rocha', '(61) 94444-0008', 'fernanda@email.com', 'Rua Y, 20'),
('Paulo Alves', '(71) 93333-0009', 'paulo@email.com', 'Rua Z, 30'),
('Juliana Mendes', '(81) 92222-0010', 'juliana@email.com', 'Av Central, 100');

-- Inserindo Veterinários
INSERT INTO Veterinario (CRMA, nome, especialidade, telefone) VALUES
('CRMV-1234', 'Dr. Andre', 'Clínica Geral', '(11) 91111-1111'),
('CRMV-5678', 'Dra. Beatriz', 'Cirurgia', '(11) 92222-2222'),
('CRMV-9012', 'Dr. Claudio', 'Dermatologia', '(11) 93333-3333'),
('CRMV-3456', 'Dra. Diana', 'Ortopedia', '(11) 94444-4444'),
('CRMV-7890', 'Dr. Eduardo', 'Cardiologia', '(11) 95555-5555'),
('CRMV-1111', 'Dra. Fabiola', 'Clínica Geral', '(11) 96666-6666'),
('CRMV-2222', 'Dr. Gustavo', 'Anestesia', '(11) 97777-7777'),
('CRMV-3333', 'Dra. Helena', 'Oftalmologia', '(11) 98888-8888'),
('CRMV-4444', 'Dr. Igor', 'Exóticos', '(11) 99999-9999'),
('CRMV-5555', 'Dra. Julia', 'Oncologia', '(11) 90000-0000');

-- Inserindo Animais
INSERT INTO Animal (nome, especie, raca, data_nascimento, peso, porte, sexo, castrado, id_Tutor) VALUES
('Rex', 'Cão', 'Labrador', '2020-01-01', 30.50, 'Grande', 'Macho', 'SIM', 1),
('Mimi', 'Gato', 'Siamês', '2019-05-10', 4.20, 'Pequeno', 'Fêmea', 'SIM', 2),
('Thor', 'Cão', 'Bulldog', '2021-03-15', 15.00, 'Médio', 'Macho', 'NÃO', 3),
('Luna', 'Gato', 'Persa', '2022-07-20', 3.80, 'Pequeno', 'Fêmea', 'NÃO', 4),
('Bob', 'Cão', 'Poodle', '2018-11-05', 6.50, 'Pequeno', 'Macho', 'SIM', 5),
('Mel', 'Cão', 'Golden', '2020-02-28', 28.00, 'Grande', 'Fêmea', 'SIM', 6),
('Fred', 'Gato', 'SRD', '2021-09-12', 5.00, 'Médio', 'Macho', 'NÃO', 7),
('Belinha', 'Cão', 'Shih Tzu', '2019-12-25', 5.50, 'Pequeno', 'Fêmea', 'SIM', 8),
('Nick', 'Cão', 'Beagle', '2020-06-30', 12.00, 'Médio', 'Macho', 'SIM', 9),
('Tom', 'Gato', 'Maine Coon', '2021-01-15', 8.50, 'Grande', 'Macho', 'NÃO', 10);

-- Inserindo Agendamentos
INSERT INTO Agendamento (data_agendamento, hora, status, id_Veterinario, id_Animal) VALUES
('2025-01-10', '10:00:00', 'CONCLUIDO', 1, 1),
('2025-01-10', '11:00:00', 'CONCLUIDO', 2, 2),
('2025-01-11', '09:00:00', 'CANCELADO', 1, 3),
('2025-01-12', '14:00:00', 'CONFIRMADO', 3, 4),
('2025-01-12', '15:00:00', 'PENDENTE', 4, 5),
('2025-01-13', '10:30:00', 'CONFIRMADO', 1, 6),
('2025-01-14', '16:00:00', 'PENDENTE', 5, 7),
('2025-01-15', '08:00:00', 'CONCLUIDO', 2, 8),
('2025-01-16', '11:00:00', 'CONFIRMADO', 3, 9),
('2025-01-17', '13:00:00', 'PENDENTE', 4, 10);

-- Inserindo Consultas
INSERT INTO Consulta (data_consulta, sintomas, diagnostico, id_Veterinario, id_Animal) VALUES
('2025-01-10', 'Vômito e diarreia', 'Gastroenterite', 1, 1),
('2025-01-10', 'Coceira na orelha', 'Otite fúngica', 2, 2),
('2025-01-15', 'Mancando pata traseira', 'Torção leve', 2, 8),
('2024-12-01', 'Tosse seca', 'Gripe canina', 1, 1),
('2024-12-05', 'Queda de pelo', 'Dermatite alérgica', 3, 9),
('2024-12-10', 'Olhos vermelhos', 'Conjuntivite', 4, 5),
('2024-12-15', 'Falta de apetite', 'Febre viral', 1, 6),
('2024-12-20', 'Ferida na pata', 'Corte superficial', 5, 7),
('2024-12-22', 'Checkup anual', 'Saudável', 1, 3),
('2024-12-28', 'Dente quebrado', 'Fratura dentária', 2, 10);

-- Inserindo Tratamentos
INSERT INTO Tratamento (descricao, data_inicio, data_fim_previsto, id_Consulta) VALUES
('Antibiótico 12h/12h', '2025-01-10', '2025-01-17', 1),
('Limpeza auricular e gotas', '2025-01-10', '2025-01-20', 2),
('Repouso e anti-inflamatório', '2025-01-15', '2025-01-18', 3),
('Xarope para tosse', '2024-12-01', '2024-12-10', 4),
('Shampoo especial e dieta', '2024-12-05', '2025-01-05', 5),
('Colírio 3x ao dia', '2024-12-10', '2024-12-17', 6),
('Soro e monitoramento', '2024-12-15', '2024-12-16', 7),
('Curativo diário', '2024-12-20', '2024-12-25', 8),
('Vacinação V8', '2024-12-22', '2024-12-22', 9),
('Extração e medicação', '2024-12-28', '2025-01-02', 10);