-- Insert into microregiao
INSERT INTO microregiao (id, nome) VALUES (1, 'Micro Região Teste');

-- Insert into pacientes
INSERT INTO pacientes (numeroSUS, data_nascimento, sexo, info, telefone, email, nome, micro_regiao_id)
VALUES (123456789, '1990-01-01', 'Masculino', 'Paciente teste', '123456789', 'paciente@teste.com', 'Paciente Teste', 1);

-- Insert into perfis
INSERT INTO perfis (id, name) VALUES (1, 'Administrador');

-- Insert into funcionarios
INSERT INTO funcionarios (id, cpf, password, nome, email, id_perfil)
VALUES (1, '12345678900', 'senha123', 'Funcionario Teste', 'funcionario@teste.com', 1);

-- Insert into tipos_exames
INSERT INTO tipos_exames (id, nome, status) VALUES (1, 'Exame de Sangue', TRUE);

-- Insert into tipos_medicamentos
INSERT INTO tipos_medicamentos (id, nome, info) VALUES (1, 'Medicamento Teste', 'Informação do medicamento');

-- Insert into medicamentos
INSERT INTO medicamentos (id, status, frequencia, dosagem, fk_tipo_medicamento, fk_paciente)
VALUES (1, 'Ativo', 'Diária', '500mg', 1, 123456789);

-- Insert into especialidades
INSERT INTO especialidades (id, nome) VALUES (1, 'Cardiologia');

-- Insert into consultas
INSERT INTO consultas (id, fk_paciente, fk_especialidade, fk_funcionario)
VALUES (1, 123456789, 1, 1);

-- Insert into estratificacoes
INSERT INTO estratificacoes (id, data, categoria, fk_paciente, fk_consulta)
VALUES (1, CURRENT_DATE, 'Alto Risco', 123456789, 1);

-- Insert into findrisk
INSERT INTO findrisk (id, data, pont_historico_familiar_de_diabetes, pont_historico_de_glicemia_elevada, classificacao, pont_idade, pont_imc, pont_circunferencia_cintura, pont_atv_fisica, pont_ingestao_frutas_e_verduras, pont_hipertensao, fk_paciente, fk_consulta)
VALUES (1, CURRENT_DATE, '2', '1', 'Moderado', '3', '2', '1', '1', '1', '1', 123456789, 1);

-- Insert into logs
INSERT INTO logs (id, timestamp, usuario_id, ip_origem, acao, tabela_afetada, registro_id, descricao, status, origem, metodo_http)
VALUES (1, CURRENT_TIMESTAMP, 1, '127.0.0.1', 'Teste de Log', 'pacientes', 123456789, 'Log de teste', 'Sucesso', 'Sistema', 'POST');

-- Insert into patologia
INSERT INTO patologia (id, nome) VALUES (1, 'Diabetes Tipo 2');

-- Insert into paciente_patologias
INSERT INTO paciente_patologias (id, fk_patologia, fk_paciente)
VALUES (1, 1, 123456789);

-- Insert into biometrias
INSERT INTO biometrias (id, imc, peso, altura, data, cintura, fk_paciente, fk_consulta)
VALUES (1, 25.0, 70.0, 1.75, CURRENT_DATE, 85.0, 123456789, 1);

-- Insert into exames
INSERT INTO exames (id, data_realizacao, resultado, fk_paciente, fk_tipo_exame, fk_consulta)
VALUES (1, '2023-10-01', 'Normal', 123456789, 1, 1);

-- Insert into permissoes
INSERT INTO permissoes (id, name) VALUES (1, 'Acesso Completo');

-- Insert into perfilpermissoes
INSERT INTO perfilpermissoes (id, id_perfil, id_permissao)
VALUES (1, 1, 1);
