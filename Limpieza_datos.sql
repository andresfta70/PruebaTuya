ALTER TABLE  test_schema.clientes ADD fecha_date DATE;

UPDATE test_schema.clientes
SET fecha_date = STR_TO_DATE(FECHA_APERTURA_TARJETA, '%Y-%m-%d');

SELECT FECHA_APERTURA_TARJETA, fecha_datetime, fecha_date FROM test_schema.clientes LIMIT 10;

ALTER TABLE test_schema.clientes DROP COLUMN FECHA_APERTURA_TARJETA;
ALTER TABLE test_schema.clientes DROP COLUMN fecha_datetime;

ALTER TABLE test_schema.clientes CHANGE COLUMN fecha_date FECHA_APERTURA_TARJETA DATE;

ALTER TABLE  test_schema.transacciones ADD fecha_date DATE;

UPDATE test_schema.transacciones
SET fecha_date = STR_TO_DATE(FECHA_TRANSACCION, '%Y-%m-%d')
WHERE FECHA_TRANSACCION <> '';

ALTER TABLE test_schema.transacciones DROP COLUMN FECHA_TRANSACCION;

ALTER TABLE test_schema.transacciones CHANGE COLUMN fecha_date FECHA_TRANSACCION DATE;

select fecha_transaccion from test_schema.transacciones;