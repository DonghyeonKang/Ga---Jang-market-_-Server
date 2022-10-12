-- 고성군 시장 데이터 -----------------------------------------------------------------------------------
INSERT INTO market(market_name, market_region, market_address, info, latitude, longitude) VALUES ('고성공룡시장', '고성군', '경남 고성군 고성읍 성내로112번길 75-8', '1910년 개장하여 100년이 넘는 역사를 가진 전통시장. 채소, 과일, 건어, 식육, 어패류, 잡화 등 130여명의 상인이 종사', 34.9725627386022, 128.32333382598);
INSERT INTO market(market_name, market_region, market_address, info, latitude, longitude) VALUES ('고성시장', '고성군', '경남 고성군 고성읍 중앙로25번길 57', '1989년부터 2002년까지 22,234㎡의 부지에 4차에 걸쳐 현대화사업을 추진 생어, 건어, 식육, 어류, 잡화부 등 총 279칸의 점포를 운영. 상설시장이나 매월 1일, 6일, 11일, 16일, 21일, 26일 5일마다 전국의 상인이 모여 개설되는 5일장의 대표시장', 34.9770287809181, 128.322912913266);
INSERT INTO market(market_name, market_region, market_address, info, latitude, longitude) VALUES ('배둔시장', '고성군', '경남 고성군 회화면 배둔로31번길 31', '1965년 개설된 전통시장. 특별한 먹거리인 염소국밥과 막걸리는 사라져 가는 농촌시장의 고향의 향수를 느낄 수 있음. 채소, 과일, 건어, 식육, 어패류, 잡화 등 40여명의 상인이 종사', 35.0574908293121, 128.369322158935);
INSERT INTO market(market_name, market_region, market_address, info, latitude, longitude) VALUES ('영오시장', '고성군', '경남 고성군 영오면 문산로 3', '1954년 12월 고성공설시장 개설 허가를 획득한 재래시장. 채소, 과일, 건어, 식육, 어패류, 잡화 등 20여명의 상인이 종사', 35.1089607498004, 128.237975490252);
-- 고성공룡시장 더미데이터
INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(3, '동현이네 고성정육점', '동현이가 파는 신선한 육고기, 돼지고기, 소고기!', 0, 07:00, 19:00);
    INSERT INTO product(s_id, product_name, price) VALUES (1,'치마살',100)
    INSERT INTO product(s_id, product_name, price) VALUES (1,'목살',100)
    INSERT INTO product(s_id, product_name, price) VALUES (1,'삼겹살',100)
    INSERT INTO product(s_id, product_name, price) VALUES (1,'갈매기살',100)

INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(3, '동현이네 고성공구상사', '세상에 모든 공구를 판매합니다.', 0, 07:00, 19:00);
    INSERT INTO product(s_id, product_name, price) VALUES (2,'드라이버',100)
    INSERT INTO product(s_id, product_name, price) VALUES (2,'나사',100)
    INSERT INTO product(s_id, product_name, price) VALUES (2,'망치',100)
    INSERT INTO product(s_id, product_name, price) VALUES (2,'도끼',100)

INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(3, '동현이네 고성옷가게', '옷가지들을 판매합니다.', 0, 07:00, 19:00);
    INSERT INTO product(s_id, product_name, price) VALUES (3,'난닝구',100)
    INSERT INTO product(s_id, product_name, price) VALUES (3,'모자',100)
    INSERT INTO product(s_id, product_name, price) VALUES (3,'츄리닝',100)
    INSERT INTO product(s_id, product_name, price) VALUES (3,'쓰레빠',100)


-- 고성시장 더미데이터
INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(3, '수민이네 고성정육점', '수민이가 파는 신선한 육고기, 돼지고기, 소고기!', 0, 07:00, 19:00);
    INSERT INTO product(s_id, product_name, price) VALUES (4,'치마살',100)
    INSERT INTO product(s_id, product_name, price) VALUES (4,'목살',100)
    INSERT INTO product(s_id, product_name, price) VALUES (4,'삼겹살',100)
    INSERT INTO product(s_id, product_name, price) VALUES (4,'갈매기살',100)

INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(3, '수민이네 고성공구상사', '세상에 모든 공구를 판매합니다.', 0, 07:00, 19:00);
    INSERT INTO product(s_id, product_name, price) VALUES (5,'드라이버',100)
    INSERT INTO product(s_id, product_name, price) VALUES (5,'나사',100)
    INSERT INTO product(s_id, product_name, price) VALUES (5,'망치',100)
    INSERT INTO product(s_id, product_name, price) VALUES (5,'도끼',100)

INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(3, '수민이네 고성옷가게', '옷가지들을 판매합니다.', 0, 07:00, 19:00);
    INSERT INTO product(s_id, product_name, price) VALUES (6,'난닝구',100)
    INSERT INTO product(s_id, product_name, price) VALUES (6,'모자',100)
    INSERT INTO product(s_id, product_name, price) VALUES (6,'츄리닝',100)
    INSERT INTO product(s_id, product_name, price) VALUES (6,'쓰레빠',100)

-- 배둔시장 더미데이터
INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(3, '수환이네 고성정육점', '수환이가 파는 신선한 육고기, 돼지고기, 소고기!', 0, 07:00, 19:00);
    INSERT INTO product(s_id, product_name, price) VALUES (7,'치마살',100)
    INSERT INTO product(s_id, product_name, price) VALUES (7,'목살',100)
    INSERT INTO product(s_id, product_name, price) VALUES (7,'삼겹살',100)
    INSERT INTO product(s_id, product_name, price) VALUES (7,'갈매기살',100)

INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(3, '수환이네 고성공구상사', '세상에 모든 공구를 판매합니다.', 0, 07:00, 19:00);
    INSERT INTO product(s_id, product_name, price) VALUES (8,'드라이버',100)
    INSERT INTO product(s_id, product_name, price) VALUES (8,'나사',100)
    INSERT INTO product(s_id, product_name, price) VALUES (8,'망치',100)
    INSERT INTO product(s_id, product_name, price) VALUES (8,'도끼',100)

INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(3, '수환이네 고성옷가게', '옷가지들을 판매합니다.', 0, 07:00, 19:00);
    INSERT INTO product(s_id, product_name, price) VALUES (9,'난닝구',100)
    INSERT INTO product(s_id, product_name, price) VALUES (9,'모자',100)
    INSERT INTO product(s_id, product_name, price) VALUES (9,'츄리닝',100)
    INSERT INTO product(s_id, product_name, price) VALUES (9,'쓰레빠',100)

-- 영오시장 더미데이터
INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(3, '시현이네 고성정육점', '시현이가 파는 신선한 육고기, 돼지고기, 소고기!', 0, 07:00, 19:00);
    INSERT INTO product(s_id, product_name, price) VALUES (10,'치마살',100)
    INSERT INTO product(s_id, product_name, price) VALUES (10,'목살',100)
    INSERT INTO product(s_id, product_name, price) VALUES (10,'삼겹살',100)
    INSERT INTO product(s_id, product_name, price) VALUES (10,'갈매기살',100)

INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(3, '시현이네 고성공구상사', '세상에 모든 공구를 판매합니다.', 0, 07:00, 19:00);
    INSERT INTO product(s_id, product_name, price) VALUES (11,'드라이버',100)
    INSERT INTO product(s_id, product_name, price) VALUES (11,'나사',100)
    INSERT INTO product(s_id, product_name, price) VALUES (11,'망치',100)
    INSERT INTO product(s_id, product_name, price) VALUES (11,'도끼',100)

INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(3, '시현이네 고성옷가게', '옷가지들을 판매합니다.', 0, 07:00, 19:00);
    INSERT INTO product(s_id, product_name, price) VALUES (12,'난닝구',100)
    INSERT INTO product(s_id, product_name, price) VALUES (12,'모자',100)
    INSERT INTO product(s_id, product_name, price) VALUES (12,'츄리닝',100)
    INSERT INTO product(s_id, product_name, price) VALUES (12,'쓰레빠',100)

-- 거제시 시장 데이터 -----------------------------------------------------------------------------------
INSERT INTO market(market_name, market_region, market_address, info, latitude, longitude) VALUES ('거제고현시장', '거제시', '경남 거제시 거제중앙로 1883-2', '고현시장이 거제도에서 가장 큰 재래시장으로 시장의 모습은 일반 재래시장과는 다르다. 일반 재래시장은 하나의 길목을 중심으로 길게 뻗어있는 모양이라면 고현시장은 총 4개의 입구와 이 모든 4개의 길목이 만나는 길목 끝에 가로형으로 큰 길목이 이어주는 형태였다. ', 34.8862671420497, 128.623658112727);
INSERT INTO market(market_name, market_region, market_address, info, latitude, longitude) VALUES ('신부시장', '거제시', '경남 거제시 장승포로 49', '거제시 장포승동에 위치한 40여 개 점포로 이루어진 소형규모의 신부시장. 그 크기는 작지만 현대식 상가로 내부가 깔끔하여 쇼핑하기에 편리하다. 맛집도 많고 주변 환경도 근사해서 찾는 이들이 많은 곳이다. 장어요리를 전문으로 하는 ‘성영시장’이라는 식당이 인기가 좋다. 몸에 좋고 맛도 좋은 다양한 생선요리를 저렴한 가격에 맛볼 수 있는 신부시장으로 떠나보자.', 34.8677614280007, 128.729542544462);
INSERT INTO market(market_name, market_region, market_address, info, latitude, longitude) VALUES ('옥수동새시장', '거제시', '경남 거제시 능포로 134-2', '거제시 능포동에 위치한 옥수동새시장. 33개 점포로 이루어진 상가건물이다. 옥수동 새시장은 1984년에 문을 열었는데, 그 역사와 함께한 맛집이 있다. 1986년부터 영업해 온 ‘옛날 쌈밥집’ .20년 넘게 그 자리에서 맛난 음식을 만들어 주시는 주인 할머님의 인정이 가득 담긴 쌈밥을 맛보러 떠나고 싶다.', 34.8753995474369, 128.731919829604);
INSERT INTO market(market_name, market_region, market_address, info, latitude, longitude) VALUES ('옥수시장', '거제시', '경남 거제시 옥수로10길 35', '거제시 능포동에 위치한 옥수시장. 110여 개 노점과 점포로 이루어진 중형규모의 상가건물형 시장이다. 주로 마늘, 갈치, 조기, 오이 등의 물품을 취급하고 있으며 이외에도 활어와 해산물, 야채, 과일 등 다양한 식자재가 풍부하다. 시장운영시간은 오전 8시부터 저녁 8시까지이다. 볼거리와 먹거리 모두 풍부한 옥수시장으로 구경 가보자.', 34.8761900720628, 128.731310321082);
INSERT INTO market(market_name, market_region, market_address, info, latitude, longitude) VALUES ('옥포국제시장', '거제시', '경남 거제시 옥포로 215', '옥포시장은 옥포시내 사거리 바로 옆에 위치하고 있었다. 입구에서부터 더운 날씨에도 햇볕을 피해 물건 파는 사람들과 사는 사람들로 북적북적했고 여기저기서 흥정하는 소리, 특이한 목소리로 구매를 유도하는 독특한 사장님! 각양각색의 사람들을 만날 수 있다. ', 34.8942677345199, 128.689964451971);

-- 거제고현시장 더미데이터
INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(3, '채준이네 거제정육점', '동현이가 파는 신선한 육고기, 돼지고기, 소고기!', 0, 07:00, 19:00);
    INSERT INTO product(s_id, product_name, price) VALUES (13,'치마살',100)
    INSERT INTO product(s_id, product_name, price) VALUES (13,'목살',100)
    INSERT INTO product(s_id, product_name, price) VALUES (13,'삼겹살',100)
    INSERT INTO product(s_id, product_name, price) VALUES (13,'갈매기살',100)

INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(3, '채준이네 거제공구상사', '세상에 모든 공구를 판매합니다.', 0, 07:00, 19:00);
    INSERT INTO product(s_id, product_name, price) VALUES (14,'드라이버',100)
    INSERT INTO product(s_id, product_name, price) VALUES (14,'나사',100)
    INSERT INTO product(s_id, product_name, price) VALUES (14,'망치',100)
    INSERT INTO product(s_id, product_name, price) VALUES (14,'도끼',100)

INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(3, '채준이네 거제옷가게', '옷가지들을 판매합니다.', 0, 07:00, 19:00);
    INSERT INTO product(s_id, product_name, price) VALUES (15,'난닝구',100)
    INSERT INTO product(s_id, product_name, price) VALUES (15,'모자',100)
    INSERT INTO product(s_id, product_name, price) VALUES (15,'츄리닝',100)
    INSERT INTO product(s_id, product_name, price) VALUES (15,'쓰레빠',100)

-- 신부시장 더미데이터
INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(3, '재형이네 거제정육점', '동현이가 파는 신선한 육고기, 돼지고기, 소고기!', 0, 07:00, 19:00);
    INSERT INTO product(s_id, product_name, price) VALUES (16,'치마살',100)
    INSERT INTO product(s_id, product_name, price) VALUES (16,'목살',100)
    INSERT INTO product(s_id, product_name, price) VALUES (16,'삼겹살',100)
    INSERT INTO product(s_id, product_name, price) VALUES (16,'갈매기살',100)

INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(3, '재형이네 거제공구상사', '세상에 모든 공구를 판매합니다.', 0, 07:00, 19:00);
    INSERT INTO product(s_id, product_name, price) VALUES (17,'드라이버',100)
    INSERT INTO product(s_id, product_name, price) VALUES (17,'나사',100)
    INSERT INTO product(s_id, product_name, price) VALUES (17,'망치',100)
    INSERT INTO product(s_id, product_name, price) VALUES (17,'도끼',100)

INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(3, '재형이네 거제옷가게', '옷가지들을 판매합니다.', 0, 07:00, 19:00);
    INSERT INTO product(s_id, product_name, price) VALUES (18,'난닝구',100)
    INSERT INTO product(s_id, product_name, price) VALUES (18,'모자',100)
    INSERT INTO product(s_id, product_name, price) VALUES (18,'츄리닝',100)
    INSERT INTO product(s_id, product_name, price) VALUES (18,'쓰레빠',100)

-- 옥수동새시장 더미데이터
INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(3, '동현이네 거제정육점', '동현이가 파는 신선한 육고기, 돼지고기, 소고기!', 0, 07:00, 19:00);
    INSERT INTO product(s_id, product_name, price) VALUES (19,'치마살',100)
    INSERT INTO product(s_id, product_name, price) VALUES (19,'목살',100)
    INSERT INTO product(s_id, product_name, price) VALUES (19,'삼겹살',100)
    INSERT INTO product(s_id, product_name, price) VALUES (19,'갈매기살',100)

INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(3, '동현이네 거제공구상사', '세상에 모든 공구를 판매합니다.', 0, 07:00, 19:00);
    INSERT INTO product(s_id, product_name, price) VALUES (20,'드라이버',100)
    INSERT INTO product(s_id, product_name, price) VALUES (20,'나사',100)
    INSERT INTO product(s_id, product_name, price) VALUES (20,'망치',100)
    INSERT INTO product(s_id, product_name, price) VALUES (20,'도끼',100)

INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(3, '동현이네 거제옷가게', '옷가지들을 판매합니다.', 0, 07:00, 19:00);
    INSERT INTO product(s_id, product_name, price) VALUES (21,'난닝구',100)
    INSERT INTO product(s_id, product_name, price) VALUES (21,'모자',100)
    INSERT INTO product(s_id, product_name, price) VALUES (21,'츄리닝',100)
    INSERT INTO product(s_id, product_name, price) VALUES (21,'쓰레빠',100)

-- 옥수시장 더미데이터
INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(3, '수민이네 거제정육점', '동현이가 파는 신선한 육고기, 돼지고기, 소고기!', 0, 07:00, 19:00);
    INSERT INTO product(s_id, product_name, price) VALUES (22,'치마살',100)
    INSERT INTO product(s_id, product_name, price) VALUES (22,'목살',100)
    INSERT INTO product(s_id, product_name, price) VALUES (22,'삼겹살',100)
    INSERT INTO product(s_id, product_name, price) VALUES (22,'갈매기살',100)

INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(3, '수민이네 거제공구상사', '세상에 모든 공구를 판매합니다.', 0, 07:00, 19:00);
    INSERT INTO product(s_id, product_name, price) VALUES (23,'드라이버',100)
    INSERT INTO product(s_id, product_name, price) VALUES (23,'나사',100)
    INSERT INTO product(s_id, product_name, price) VALUES (23,'망치',100)
    INSERT INTO product(s_id, product_name, price) VALUES (23,'도끼',100)

INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(3, '수민이네 거제옷가게', '옷가지들을 판매합니다.', 0, 07:00, 19:00);
    INSERT INTO product(s_id, product_name, price) VALUES (24,'난닝구',100)
    INSERT INTO product(s_id, product_name, price) VALUES (24,'모자',100)
    INSERT INTO product(s_id, product_name, price) VALUES (24,'츄리닝',100)
    INSERT INTO product(s_id, product_name, price) VALUES (24,'쓰레빠',100)

-- 옥포국제시장 더미데이터
INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(3, '가은이네 거제정육점', '동현이가 파는 신선한 육고기, 돼지고기, 소고기!', 0, 07:00, 19:00);
    INSERT INTO product(s_id, product_name, price) VALUES (25,'치마살',100)
    INSERT INTO product(s_id, product_name, price) VALUES (25,'목살',100)
    INSERT INTO product(s_id, product_name, price) VALUES (25,'삼겹살',100)
    INSERT INTO product(s_id, product_name, price) VALUES (25,'갈매기살',100)


INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(3, '가은이네 거제공구상사', '세상에 모든 공구를 판매합니다.', 0, 07:00, 19:00);
    INSERT INTO product(s_id, product_name, price) VALUES (26,'드라이버',100)
    INSERT INTO product(s_id, product_name, price) VALUES (26,'나사',100)
    INSERT INTO product(s_id, product_name, price) VALUES (26,'망치',100)
    INSERT INTO product(s_id, product_name, price) VALUES (26,'도끼',100)

INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(3, '가은이네 거제옷가게', '옷가지들을 판매합니다.', 0, 07:00, 19:00);
    INSERT INTO product(s_id, product_name, price) VALUES (27,'난닝구',100)
    INSERT INTO product(s_id, product_name, price) VALUES (27,'모자',100)
    INSERT INTO product(s_id, product_name, price) VALUES (27,'츄리닝',100)
    INSERT INTO product(s_id, product_name, price) VALUES (27,'쓰레빠',100)

-- 남해군 시장 데이터 -----------------------------------------------------------------------------------
INSERT INTO market(market_name, market_region, market_address, info, latitude, longitude) VALUES ('남면공설시장', '남해군', '경남 남해군 남면 남서대로 785-4', '남해군 남면 당항리에 위치한 공설시장. ‘시골 시장’이라는 말이 잘 어울리는 시골 장터의 분위기가 물씬 풍기는 곳이다. 정성스레 손질된 물건들과 한적한 시골 마을의 분위기, 따뜻하고 인정 많은 어르신들이 있어 편안한 분위기의 시장이다. 50년 넘는 전통과 역사를 간직한 정겨움이 넘실대는 남면공설시장으로 떠나보자. ', 34.7712467130909, 127.88600651682);
INSERT INTO market(market_name, market_region, market_address, info, latitude, longitude) VALUES ('남해전통시장', '남해군', '경남 남해군 남해읍 북변리 282-11', '남해전통시장은 현재 상설시장으로 운영되고 있지만, 끝자리가 2일, 7일인 날(2일, 7일, 12일, 17일, 22일, 27일)에는 규모 있게 장이 서는 전통시장이다.', 34.8411389602405, 127.894364048496);
INSERT INTO market(market_name, market_region, market_address, info, latitude, longitude) VALUES ('이동전통시장', '남해군', '경남 남해군 이동면 무림로 59-3', '남해군 이동면 무림리에 위치한 공설시장. 24개 점포로 이루어져 그 규모가 작은 소형시장이지만, 1933년부터 자리를 지키며 80년 넘게 그 전통을 이어온 곳이다. 그 세월만큼이나 크게 느껴지는 따뜻한 정과 상인들의 후한 인심이 넘치는 시장이다. 주차시설도 갖추고 있어서 편리하게 장을 볼 수 있다.', 34.8006657450975, 127.953639382788);

-- 남면공설시장 더미데이터
INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(3, '가은이네 남해라면트럭', '가은이가 만든 맛있는 마약 라면을 파는 식당입니다!', 0, 07:00, 19:00);
    INSERT INTO product(s_id, product_name, price) VALUES (28,'진라면',100)
    INSERT INTO product(s_id, product_name, price) VALUES (28,'신라면',100)
    INSERT INTO product(s_id, product_name, price) VALUES (28,'안성탕면',100)
    INSERT INTO product(s_id, product_name, price) VALUES (28,'우육면',100)

INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(3, '민제네 남해오리고기', '가은이가 만든 맛있는 오리고기를 파는 식당입니다!', 0, 07:00, 19:00);
    INSERT INTO product(s_id, product_name, price) VALUES (29,'오리고기 정식',100)
    INSERT INTO product(s_id, product_name, price) VALUES (29,'오리고기 한입',100)
    INSERT INTO product(s_id, product_name, price) VALUES (29,'오리고기 샤브샤브',100)
    INSERT INTO product(s_id, product_name, price) VALUES (29,'오리고기 마라탕',100)

INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(3, '동현이네 남해옷가게', '가은이가 공수해온 값싼 옷을 파는 가게입니다!', 0, 07:00, 19:00);
    INSERT INTO product(s_id, product_name, price) VALUES (30,'난닝구',100)
    INSERT INTO product(s_id, product_name, price) VALUES (30,'모자',100)
    INSERT INTO product(s_id, product_name, price) VALUES (30,'신발',100)
    INSERT INTO product(s_id, product_name, price) VALUES (30,'쓰레빠',100)

-- 남해전통시장 더미데이터
INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(3, '가은네 남해라면트럭', '민제가 만든 맛있는 마약 라면을 파는 가게입니다!', 0, 07:00, 19:00);
    INSERT INTO product(s_id, product_name, price) VALUES (31,'진라면',100)
    INSERT INTO product(s_id, product_name, price) VALUES (31,'신라면',100)
    INSERT INTO product(s_id, product_name, price) VALUES (31,'안성탕면',100)
    INSERT INTO product(s_id, product_name, price) VALUES (31,'우육면',100)

INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(3, '민제네 남해오리고기', '오리는 꽥꽥 민제내 남해오리고기 많이 찾아주세요!', 0, 07:00, 19:00);
    INSERT INTO product(s_id, product_name, price) VALUES (32,'오리고기 정식',100)
    INSERT INTO product(s_id, product_name, price) VALUES (32,'오리고기 한입',100)
    INSERT INTO product(s_id, product_name, price) VALUES (32,'오리고기 샤브샤브',100)
    INSERT INTO product(s_id, product_name, price) VALUES (32,'오리고기 마라탕',100)

INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(3, '동현네 남해옷가게', '싸다싸 민제 옷가게!', 0, 07:00, 19:00);
    INSERT INTO product(s_id, product_name, price) VALUES (33,'난닝구',100)
    INSERT INTO product(s_id, product_name, price) VALUES (33,'모자',100)
    INSERT INTO product(s_id, product_name, price) VALUES (33,'츄리닝',100)
    INSERT INTO product(s_id, product_name, price) VALUES (33,'쓰레빠',100)

-- 이동전통시장 더미데이터
INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(3, '가은이네 남해정육점', '동현이가 파는 신선한 육고기, 돼지고기, 소고기!', 0, 07:00, 19:00);
    INSERT INTO product(s_id, product_name, price) VALUES (34,'치마살',100)
    INSERT INTO product(s_id, product_name, price) VALUES (34,'목살',100)
    INSERT INTO product(s_id, product_name, price) VALUES (34,'삼겹살',100)
    INSERT INTO product(s_id, product_name, price) VALUES (34,'갈매기살',100)

INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(3, '민제네 남해공구상사', '세상에 모든 공구를 판매합니다.', 0, 07:00, 19:00);
    INSERT INTO product(s_id, product_name, price) VALUES (35,'드라이버',100)
    INSERT INTO product(s_id, product_name, price) VALUES (35,'나사',100)
    INSERT INTO product(s_id, product_name, price) VALUES (35,'망치',100)
    INSERT INTO product(s_id, product_name, price) VALUES (35,'도끼',100)

INSERT INTO store(m_id, store_name, info, store_type, open_time, close_time) VALUES(3, '동현이네 남해옷가게', '옷가지들을 판매합니다.', 0, 07:00, 19:00);
    INSERT INTO product(s_id, product_name, price) VALUES (36,'난닝구',100)
    INSERT INTO product(s_id, product_name, price) VALUES (36,'모자',100)
    INSERT INTO product(s_id, product_name, price) VALUES (36,'츄리닝',100)
    INSERT INTO product(s_id, product_name, price) VALUES (36,'쓰레빠',100)