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
INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(1, '경아 식육점', '동현이가 파는 신선한 육고기, 돼지고기, 소고기!', 0, '07:00', '19:00');
INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(1, '식이 건어물', '세상에 모든 공구를 판매합니다.', 0, '07:00', '19:00');
INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(1, '영광 잡화', '옷가지들을 판매합니다.', 0, '07:00', '19:00');
INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(1, '영일 상회', '오늘 들여온 야채, 채소를 판매합니다! 싱싱하게 좋은 것들로만 골랐으니, 많이들 사가이소~', 0, '07:00', '19:00');
INSERT INTO store_img(s_id, img_path) VALUES (1, "");
INSERT INTO store_img(s_id, img_path) VALUES (1, "");
INSERT INTO store_img(s_id, img_path) VALUES (1, "");
INSERT INTO product(s_id, product_name, price) VALUES (1,'치마살',100);
INSERT INTO product(s_id, product_name, price) VALUES (1,'목살',100);
INSERT INTO product(s_id, product_name, price) VALUES (1,'삼겹살',100);
INSERT INTO product(s_id, product_name, price) VALUES (1,'갈매기살',100);
INSERT INTO product(s_id, product_name, price) VALUES (2,'드라이버',100);
INSERT INTO product(s_id, product_name, price) VALUES (2,'나사',100);
INSERT INTO product(s_id, product_name, price) VALUES (2,'망치',100);
INSERT INTO product(s_id, product_name, price) VALUES (2,'도끼',100);
INSERT INTO product(s_id, product_name, price) VALUES (3,'난닝구',100);
INSERT INTO product(s_id, product_name, price) VALUES (3,'모자',100);
INSERT INTO product(s_id, product_name, price) VALUES (3,'츄리닝',100);
INSERT INTO product(s_id, product_name, price) VALUES (3,'쓰레빠',100);
INSERT INTO product_img(s_id, p_id, img_path) VALUES (1, 1, "");
INSERT INTO product_img(s_id, p_id, img_path) VALUES (1, 1, "");
INSERT INTO product_img(s_id, p_id, img_path) VALUES (1, 1, "");
INSERT INTO product_img(s_id, p_id, img_path) VALUES (1, 1, "");
INSERT INTO product_img(s_id, p_id, img_path) VALUES (1, 2, "");
INSERT INTO product_img(s_id, p_id, img_path) VALUES (1, 2, "");
INSERT INTO product_img(s_id, p_id, img_path) VALUES (1, 2, "");
INSERT INTO product_img(s_id, p_id, img_path) VALUES (1, 2, "");
INSERT INTO product_img(s_id, p_id, img_path) VALUES (1, 3, "");
INSERT INTO product_img(s_id, p_id, img_path) VALUES (1, 3, "");
INSERT INTO product_img(s_id, p_id, img_path) VALUES (1, 3, "");
INSERT INTO product_img(s_id, p_id, img_path) VALUES (1, 3, "");

-- 하동군 시장 데이터 -----------------------------------------------------------------------------------
-- 화개장터 시장 더미데이터
INSERT INTO market(market_name, market_region, market_address, info, latitude, longitude) VALUES ('고성공룡시장', '고성군', '경남 고성군 고성읍 성내로112번길 75-8', '1910년 개장하여 100년이 넘는 역사를 가진 전통시장. 채소, 과일, 건어, 식육, 어패류, 잡화 등 130여명의 상인이 종사', 34.9725627386022, 128.32333382598);
