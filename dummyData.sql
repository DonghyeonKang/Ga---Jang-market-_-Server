-- 고성군 시장 데이터 -----------------------------------------------------------------------------------
INSERT INTO market(market_name, market_region, market_address, info, latitude, longitude) VALUES ('고성공룡시장', '고성군', '경남 고성군 고성읍 성내로112번길 75-8', '1910년 개장하여 100년이 넘는 역사를 가진 전통시장. 채소, 과일, 건어, 식육, 어패류, 잡화 등 130여명의 상인이 종사', 34.9725627386022, 128.32333382598);
INSERT INTO market(market_name, market_region, market_address, info, latitude, longitude) VALUES ('고성시장', '고성군', '경남 고성군 고성읍 중앙로25번길 57', '1989년부터 2002년까지 22,234㎡의 부지에 4차에 걸쳐 현대화사업을 추진 생어, 건어, 식육, 어류, 잡화부 등 총 279칸의 점포를 운영. 상설시장이나 매월 1일, 6일, 11일, 16일, 21일, 26일 5일마다 전국의 상인이 모여 개설되는 5일장의 대표시장', 34.9770287809181, 128.322912913266);
INSERT INTO market(market_name, market_region, market_address, info, latitude, longitude) VALUES ('배둔시장', '고성군', '경남 고성군 회화면 배둔로31번길 31', '1965년 개설된 전통시장. 특별한 먹거리인 염소국밥과 막걸리는 사라져 가는 농촌시장의 고향의 향수를 느낄 수 있음. 채소, 과일, 건어, 식육, 어패류, 잡화 등 40여명의 상인이 종사', 35.0574908293121, 128.369322158935);
INSERT INTO market(market_name, market_region, market_address, info, latitude, longitude) VALUES ('영오시장', '고성군', '경남 고성군 영오면 문산로 3', '1954년 12월 고성공설시장 개설 허가를 획득한 재래시장. 채소, 과일, 건어, 식육, 어패류, 잡화 등 20여명의 상인이 종사', 35.1089607498004, 128.237975490252);
INSERT INTO market_img(m_id, img_path) VALUES (1, "");
INSERT INTO market_img(m_id, img_path) VALUES (2, "");
INSERT INTO market_img(m_id, img_path) VALUES (3, "");
INSERT INTO market_img(m_id, img_path) VALUES (4, "");

-- 고성공룡시장 더미데이터
-- 1. 과일 및 채소 2. 음식 3. 고기류 4. 해산물 5. 의류 및 생필품 6. 기타
INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time, phone) VALUES(2, '경아 식육점', '신선한 육고기, 돼지고기, 소고기 싸게싸게 좋은 부위들로만 골라드리겠습니다! ', 3, '07:00', '19:00', "010-1234-5678");
INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time, phone) VALUES(2, '유성 식육점', '고성에서 잡은 돼지랑 소고기 팝니다.', 3, '07:00', '19:00', "010-1234-5678");
INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time, phone) VALUES(2, '가야 부식', '채소 팝니다. 무, 고추, 배추, 쪽파, 대파, 고구마, 감자', 1, '07:00', '19:00', "010-1234-5678");
INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time, phone) VALUES(2, '연일 상회', '오늘 들여온 야채, 채소를 판매합니다! 싱싱하게 좋은 것들로만 골랐으니, 많이들 사가이소~', 1, '07:00', '19:00', "010-1234-5678");
INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time, phone) VALUES(2, '수민 과일가게', '사과, 배, 복숭아, 수박, 포도 제철 과일 팔이용~~~', 1, '07:00', '19:00', "010-1234-5678");
INSERT INTO product(s_id, product_name, price) VALUES (1,'치마살', 1000);
INSERT INTO product(s_id, product_name, price) VALUES (1,'목살', 1000);
INSERT INTO product(s_id, product_name, price) VALUES (1,'삼겹살', 2000);
INSERT INTO product(s_id, product_name, price) VALUES (1,'갈매기살', 1000);

INSERT INTO product(s_id, product_name, price) VALUES (2,'뒷고기', 1000);
INSERT INTO product(s_id, product_name, price) VALUES (2,'돼지목살', 1000);
INSERT INTO product(s_id, product_name, price) VALUES (2,'삼겹살', 1000);
INSERT INTO product(s_id, product_name, price) VALUES (2,'부채살', 1000);

INSERT INTO product(s_id, product_name, price) VALUES (3,'무', 1100);
INSERT INTO product(s_id, product_name, price) VALUES (3,'고추', 1400);
INSERT INTO product(s_id, product_name, price) VALUES (3,'배추', 1300);
INSERT INTO product(s_id, product_name, price) VALUES (3,'대파', 1000);

INSERT INTO product(s_id, product_name, price) VALUES (4,'토마토', 1000);
INSERT INTO product(s_id, product_name, price) VALUES (4,'시금치', 1000);
INSERT INTO product(s_id, product_name, price) VALUES (4,'마늘', 1000);

INSERT INTO product(s_id, product_name, price) VALUES (5,'감', 20000);
INSERT INTO product(s_id, product_name, price) VALUES (5,'사과', 20000);
INSERT INTO product(s_id, product_name, price) VALUES (5,'배', 30000);
INSERT INTO product(s_id, product_name, price) VALUES (5,'복숭아', 30000);
-- 하동군 시장 데이터 -----------------------------------------------------------------------------------
-- 화개장터 시장 더미데이터
INSERT INTO market(market_name, market_region, market_address, info, latitude, longitude) VALUES ('화개장터', '하동군', '경남 하동군 화개면 쌍계로 15', '김동리의 소설 역마의 배경이 된 곳으로도 유명한 화개장터는 영호남의 접경에 위치하여 남해안의 수산물과 소금, 비옥한 호남평야의 곡물, 지리산록의 산채와 목기류가 있다. ', 35.1879096402907, 127.624250686405);

-- 1. 과일 및 채소 2. 음식 3. 고기류 4. 해산물 5. 의류 및 생필품 6. 기타
INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time, phone) VALUES(2, '애비 국밥', '이 애비가 국밥을 맛있게 말아들이오리다~ 돼지국밥, 순대국밥', 2, '07:00', '19:00', "010-1234-5678");
INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time, phone) VALUES(2, '시골집 청국장', '청국장을 맛있게 만들어 드립니당~~', 2, '07:00', '19:00', "010-1234-5678");
INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time, phone) VALUES(2, '박가네 장터', '옷, 장갑, 모자, 낫, 호미 다 판데이~', 5, '07:00', '19:00', "010-1234-5678");
INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time, phone) VALUES(2, '산골 상회', '몸빼, 티샤츠, 꽃신, 잠바 헐케 팔고 있습니다.', 5, '07:00', '19:00', "010-1234-5678");
INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time, phone) VALUES(2, '설희네', '장갑, 수건, 작업복, 머리띠, 고무신, 모자 많이들 사가세요!', 5, '07:00', '19:00', "010-1234-5678");

INSERT INTO product(s_id, product_name, price) VALUES (6,'돼지국밥', 100);
INSERT INTO product(s_id, product_name, price) VALUES (6,'내장국밥', 100);

INSERT INTO product(s_id, product_name, price) VALUES (7,'청국장', 100);

INSERT INTO product(s_id, product_name, price) VALUES (8,'몸빼', 100);
INSERT INTO product(s_id, product_name, price) VALUES (8,'티샤츠', 100);
INSERT INTO product(s_id, product_name, price) VALUES (8,'꽃신', 100);
INSERT INTO product(s_id, product_name, price) VALUES (8,'잠바', 100);

INSERT INTO product(s_id, product_name, price) VALUES (9,'장갑', 100);
INSERT INTO product(s_id, product_name, price) VALUES (9,'수건', 100);
INSERT INTO product(s_id, product_name, price) VALUES (9,'작업복', 100);