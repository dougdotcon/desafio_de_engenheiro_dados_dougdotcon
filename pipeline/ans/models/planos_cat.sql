SELECT
    CASE
        WHEN cd_contr = 1 THEN 'Individual ou Familiar'
        WHEN cd_contr = 2 THEN 'Coletivo Empresarial'
        WHEN cd_contr = 3 THEN 'Coletivo por adesão'
        WHEN cd_contr = 4 THEN 'Coletivo não identificado'
        ELSE 'Não Informado'
    END AS tipo_plano,
    SUM(qtd_planos) as total_planos
FROM dados_brutos
WHERE EXTRACT(YEAR FROM date) = 2019 AND EXTRACT(MONTH FROM date) = 12
GROUP BY cd_contr
ORDER BY cd_contr;