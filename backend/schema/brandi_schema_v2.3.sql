drop database brandi;

create database brandi character set utf8mb4 collate utf8mb4_general_ci;
use brandi;

SET time_zone='Asia/Seoul';

-- products Table Create SQL
CREATE TABLE products
(
    `product_no`  INT         NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `created_at`  DATETIME    NOT NULL    DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시', 
    `is_deleted`  TINYINT     NOT NULL    DEFAULT FALSE COMMENT '삭제여부', 
    `product_code`  VARCHAR(50)    NOT NULL    COMMENT '상품 코드',
    PRIMARY KEY (product_no)
);

INSERT INTO products
(
    product_no,
    product_code
) VALUES (
    1,
   '447acee5-1a6f-45d3-a630-fa9db6cec51a' 
), (
    2,
    'cd998fc3-43cc-4f3b-9a70-b2ad67fde612'
), (
    3,
    '34059e97-775d-4176-8b9c-467687e28fa6'
), (
    4,
    'cd5c18b2-ffba-4b70-98a5-1ff76c9b4cf8'
), (
    5,
    'd2be6842-23c4-48af-b667-32046585b292'
), (
    6,
    '63caf721-0bcb-415d-80b5-7fc6852f9e5e'
), (
    7,
    '7ac1f9c4-e34e-4013-a8ff-fd7e8d34cb8a'
), (
    8,
    '8d0e3b90-2a27-40af-8a2a-92e14b05402d'
), (
    9,
    '0839b2c9-e741-41d6-bed8-eb10c034478d'
), (
    10,
    'edbdbe99-2011-4d4b-ac1d-6b24b25b01b6'
), (
    11,
    '5ae73934-d0e4-4cff-8785-d973f7ec0553'
), (
    12,
    'd75475e3-4a30-43b6-96b2-a9e71e23044c'
), (
    13,
    'd5549f63-48fd-4c0c-b70d-521a677d7bae'
), (
    14,
    '715fbe44-7109-48c1-83c6-7f55789a44ea'
), (
    15,
    '0a8ed894-7489-4bfb-9b28-88aa8a760e80'
), (
    16,
    '7b12a5a3-99c2-4f36-b8dc-c2ceb764cd4e'
), (
    17,
    '0d5ed9ae-bd8d-4974-907c-927d1858fd2e'
), (
    18,
    'cc0bc286-f632-438a-8117-f6e106c61ca3'
), (
    19,
    'aa616244-ec2c-4d0e-8d37-595b238df355'
), (
    20,
    '5ca04d97-8178-40ea-8cc8-d3f20a5640d4'
);

-- colors Table Create SQL
CREATE TABLE colors
(
    `color_no`  INT             NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `name`      VARCHAR(50)    NOT NULL    COMMENT '색상명', 
    PRIMARY KEY (color_no)
);

ALTER TABLE colors COMMENT '색상 옵션';

INSERT INTO colors
(
    color_no,
    name
) VALUES (
    1,
    '블랙'
), (
    2,
    '화이트'
), (
    3,
    '그레이'
), (
    4,
    '아이보리'
), (
    5,
    '네이비'
), (
    6,
    '블루'
), (
    7,
    '레드'
), (
    8,
    '핑크'
), (
    9,
    '옐로우'
), (
    10,
    '베이지'
), (
    11,
    '연청'
), (
    12,
    '민트'
), (
    13,
    '진청'
), (
    14,
    '연베이지'
), (
    15,
    '중청'
), (
    16,
    '소라'
), (
    17,
    '그린'
), (
    18,
    '연퍼플'
), (
    19,
    '머스터드'
), (
    20,
    '퍼플'
), (
    21,
    '청록'
), (
    22,
    '딥핑크'
), (
    23,
    '인디핑크'
), (
    24,
    '딥그린'
), (
    25,
    '카키'
), (
    26,
    '와인'
), (
    27,
    '브라운'
), (
    28,
    '실버'
), (
    29,
    '크림'
), (
    30,
    '차콜'
), (
    31,
    '오렌지'
), (
    32,
    '올리브'
), (
    33,
    '라이트베이지'
), (
    34,
    '다크베이지'
), (
    35,
    '골드'
), (
    36,
    '라임'
), (
    37,
    '라이트블루'
), (
    38,
    '피치핑크'
), (
    39,
    '오트밀'
);


-- sizes Table Create SQL
CREATE TABLE sizes
(
    `size_no`  INT            NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `name`     VARCHAR(50)    NOT NULL    COMMENT '사이즈명', 
    PRIMARY KEY (size_no)
);

ALTER TABLE sizes COMMENT '사이즈 옵션';

INSERT INTO sizes
(
    size_no,
    name
) VALUES (
    1,
    'Free'
), (
    2,
    'XL'
), (
    3,
    'L'
), (
    4,
    'M'
), (
    5,
    'S'
), (
    6,
    'XS'
), (
    7,
    25
), (
    8,
    26
), (
    9,
    27
), (
    10,
    28
), (
    11,
    29
), (
    12,
    30
), (
    13,
    32
), (
    14,
    34
), (
    15,
    35
), (
    16,
    36
), (
    17,
    37
), (
    18,
    38
), (
    19,
    39
), (
    20,
    40
), (
    21,
    85
), (
    22,
    90
), (
    23,
    95
), (
    24,
    100
), (
    25,
    105
), (
    26,
    'XXL'
), (
    27,
    'XXXL'
), (
    28,
    'XXXXL'
), (
    29,
    'M(44-55)'
), (
    30,
    'L(55-66)'
), (
    31,
    'L(55-마른66)'
), (
    32,
    210
), (
    33,
    215
), (
    34,
    220
), (
    35,
    225
), (
    36,
    230
), (
    37,
    235
), (
    38,
    240
), (
    39,
    245
), (
    40,
    250
), (
    41,
    255
), (
    42,
    260
), (
    43,
    265
), (
    44,
    270
), (
    45,
    275
), (
    46,
    280
), (
    47,
    285
), (
    48,
    290
), (
    49,
    '1호'
), (
    50,
    '2호'
), (
    51,
    '3호'
), (
    52,
    '4호'
), (
    53,
    '5호'
), (
    54,
    '6호'
), (
    55,
    '7호'
), (
    56,
    '8호'
), (
    57,
    '9호'
), (
    58,
    '10호'
), (
    59,
    '11호'
), (
    60,
    '12호'
), (
    61,
    '13호'
), (
    62,
    '14호'
), (
    63,
    '15호'
), (
    64,
    '16호'
), (
    65,
    '17호'
), (
    66,
    '18호'
), (
    67,
    '19호'
), (
    68,
    '70a'
), (
    69,
    '70b'
), (
    70,
    '70c'
), (
    71,
    '70d'
), (
    72,
    '70e'
), (
    73,
    '70f'
), (
    74,
    '70g'
), (
    75,
    '75a'
), (
    76,
    '75b'
), (
    77,
    '75c'
), (
    78,
    '75d'
), (
    79,
    '75e'
), (
    80,
    '75f'
), (
    81,
    '75g'
), (
    82,
    '80a'
), (
    83,
    '80b'
), (
    84,
    '80c'
), (
    85,
    '80d'
), (
    86,
    '80e'
), (
    87,
    '80f'
), (
    88,
    '80g'
), (
    89,
    '85a'
), (
    90,
    '85b'
), (
    91,
    '85c'
), (
    92,
    '85d'
), (
    93,
    '85e'
), (
    94,
    '85f'
), (
    95,
    '85g'
), (
    96,
    '90a'
), (
    97,
    '90b'
), (
    98,
    '90c'
), (
    99,
    '90d'
), (
    100,
    '90e'
), (
    101,
    '90f'
), (
    102,
    '90g'
), (
    103,
    '95a'
), (
    104,
    '95b'
), (
    105,
    '95c'
), (
    106,
    '95d'
), (
    107,
    '95e'
), (
    108,
    '95f'
), (
    109,
    '95g'
), (
    110,
    '100a'
), (
    111,
    '100b'
), (
    112,
    '100c'
), (
    113,
    '100d'
), (
    114,
    '100e'
), (
    115,
    '100f'
), (
    116,
    '100g'
), (
    117,
    '105a'
), (
    118,
    '105b'
), (
    119,
    '105c'
), (
    120,
    '105d'
), (
    121,
    '105e'
), (
    122,
    '105f'
), (
    123,
    '105g'
), (
    124,
    '아이폰8'
), (
    125,
    '아이폰8플러스'
), (
    126,
    '아이폰X'
), (
    127,
    '갤럭시S9'
), (
    128,
    '갤럭시S9플러스'
);

-- social_networks Table Create SQL
CREATE TABLE social_networks
(
    `social_network_no`  INT            NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `name`               VARCHAR(45)    NOT NULL    COMMENT '소셜 이름', 
    PRIMARY KEY (social_network_no)
);

INSERT INTO social_networks
(
    social_network_no,
    name
) VALUES (
    1,
    '구글'
);

-- users Table Create SQL
CREATE TABLE users
(
    `user_no`         INT             NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `name`            VARCHAR(50)     NOT NULL    COMMENT '회원명', 
    `email`           VARCHAR(255)    NOT NULL    UNIQUE COMMENT '이메일',
    `password`        VARCHAR(50)     NULL        COMMENT '비밀번호', 
    `created_at`      DATETIME        NOT NULL    DEFAULT CURRENT_TIMESTAMP COMMENT '등록일', 
    `last_access`     DATETIME        NOT NULL    DEFAULT CURRENT_TIMESTAMP COMMENT '최종접속일', 
    `social_id`       INT             NULL        COMMENT '소셜 종류_id', 
    `user_social_id`  VARCHAR(50)     NULL        COMMENT '유저_소셜_id', 
    `is_deleted`      TINYINT         NOT NULL    DEFAULT FALSE COMMENT '삭제여부', 
    PRIMARY KEY (user_no)
);

ALTER TABLE users
    ADD CONSTRAINT FK_social_id FOREIGN KEY (social_id)
        REFERENCES social_networks (social_network_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

INSERT INTO users
(
    user_no,
    name,
    email,
    password,
    created_at
) VALUES (
    1,
    '손수정',
    'soojung@soojung.com',
    123456,
    '2020-03-01 12:00:00'
), (
    2,
    '이곤호',
    'gonho@gonho.com',
    123456,
    '2020-03-01 12:00:00'
), (
    3,
    '이민호',
    'minho@minho.com',
    123456,
    '2020-03-01 12:00:00'
), (
    4,
    '김경배',
    'rudqo@rudqo.com',
    123456,
    '2020-03-01 12:00:00'
), (
    5,
    '배정규',
    'junggyoo@junggyoo.com',
    123456,
    '2020-03-01 12:00:00'
);

-- main_categories Table Create SQL
CREATE TABLE main_categories
(
    `main_category_no`  INT            NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `name`              VARCHAR(50)    NOT NULL    COMMENT '카테고리명', 
    PRIMARY KEY (main_category_no)
);

ALTER TABLE main_categories COMMENT '1차 카테고리';

INSERT INTO main_categories
(
    main_category_no,
    name
) VALUES (
    1,
    '아우터'
), (
    2,
    '상의'
), (
    3,
    '바지'
), (
    4,
    '원피스'
), (
    5,
    '스커트'
), (
    6,
    '신발'
), (
    7,
    '가방'
), (
    8,
    '주얼리'
), (
    9,
    '잡화'
), (
    10,
    '라이프웨어'
), (
    11,
    '빅사이즈'
);

-- option_details Table Create SQL
CREATE TABLE product_options
(
    `product_option_no`  INT         NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `product_id`         INT         NOT NULL    COMMENT '상품_id', 
    `color_id`           INT         NOT NULL    COMMENT '색상_id', 
    `size_id`            INT         NOT NULL    COMMENT '사이즈_id', 
    `current_quantity`           INT         NOT NULL    COMMENT '재고',
    `created_at`         DATETIME    NOT NULL    DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시', 
    `deleted_at`         DATETIME    NULL        COMMENT '삭제일시',
    `is_deleted`         TINYINT     NOT NULL    DEFAULT FALSE COMMENT '삭제여부', 
    PRIMARY KEY (product_option_no)
);

ALTER TABLE product_options COMMENT '상품_옵션';

ALTER TABLE product_options
    ADD CONSTRAINT FK_product_options_color_id_colors_color_no FOREIGN KEY (color_id)
        REFERENCES colors (color_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE product_options
    ADD CONSTRAINT FK_product_options_size_id_sizes_size_no FOREIGN KEY (size_id)
        REFERENCES sizes (size_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE product_options
    ADD CONSTRAINT FK_product_id FOREIGN KEY (product_id)
        REFERENCES products (product_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

INSERT INTO product_options
(
    product_option_no,
    product_id,
    color_id,
    size_id,
    current_quantity
) VALUES (
    1,
    1,
    1,
    1,
    30
), (
    2,
    2,
    3,
    3,
    40
), (
    3,
    3,
    3,
    3,
    50
), (
    4,
    4,
    3,
    3,
    100
), (
    5,
    5,
    3,
    3,
    150
), (
    6,
    1,
    8,
    8,
    150
), (
    7,
    7,
    3,
    3,
    150
), (
    8,
    8,
    3,
    3,
    2000
), (
    9,
    9,
    3,
    3,
    150
), (
    10,
    10,
    3,
    3,
    1500
), (
    11,
    11,
    3,
    3,
    1300
), (
    12,
    12,
    3,
    3,
    46
), (
    13,
    13,
    3,
    3,
    17
), (
    14,
    14,
    3,
    3,
    13
), (
    15,
    15,
    3,
    3,
    100
), (
    16,
    16,
    3,
    3,
    1234
), (
    17,
    17,
    3,
    3,
    345
), (
    18,
    18,
    3,
    3,
    856
), (
    19,
    19,
    3,
    3,
    935
), (
    20,
    20,
    3,
    3,
    375
), (
    21,
    1,
    1,
    2,
    12
), (
    22,
    1,
    1,
    3,
    1212
), (
    23,
    1,
    1,
    4,
    3000
), (
    24,
    1,
    1,
    5,
    300
), (
    25,
    1,
    2,
    3,
    77
), (
    26,
    1,
    2,
    4,
    150
), (
    27,
    1,
    2,
    5,
    99
), (
    28,
    1,
    3,
    3,
    20
);

-- user_shipping_details Table Create SQL
CREATE TABLE user_shipping_details
(
    `user_shipping_detail_no`  INT             NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `user_id`                  INT             NOT NULL    COMMENT '유저_id', 
    `address`                  VARCHAR(500)    NOT NULL    COMMENT '배송지', 
    `additional_address`       VARCHAR(100)    NOT NULL    COMMENT '나머지 주소',
    `zip_code`                 VARCHAR(10)     NOT NULL    COMMENT '우편번호',
    `receiver`                 VARCHAR(50)     NOT NULL    COMMENT '수령자명', 
    `phone_number`             VARCHAR(50)     NOT NULL    COMMENT '휴대폰번호', 
    PRIMARY KEY (user_shipping_detail_no)
);

ALTER TABLE user_shipping_details
    ADD CONSTRAINT FK_user_id FOREIGN KEY (user_id)
        REFERENCES users (user_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

INSERT INTO user_shipping_details
(
    user_shipping_detail_no,
    user_id,
    address,
    additional_address,
    receiver,
    phone_number,
    zip_code
) VALUES (
    1,
    1,
    '서울특별시 강남구 테헤란로 32길 26',
    '청송빌딩 브랜디',
    '손수정수령',
    '01012345678',
    '42535'
), (
    2,
    2,
    '서울특별시 강남구 테헤란로 427, 위워크타워',
    '위코드',
    '이곤호수령',
    '01012345678',
    '54436'
), (
    3,
    3,
    '서울특별시 강남구 테헤란로 32길 26',
    '청송빌딩 브랜디',
    '이민호수령',
    '01022223333',
    '15279'
), (
    4,
    4,
    '서울특별시',
    '서울 어딘가',
    '김경배수령',
    '01033334444',
    '86352'
), (
    5,
    5,
    '서울특별시',
    '서울 어딘가',
    '배정규수령',
    '01044445555',
    '10001'
);

-- order_status Table Create SQL
CREATE TABLE order_status
(
    `order_status_no`   INT            NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `name`              VARCHAR(50)    NOT NULL    COMMENT '주문상태', 
    PRIMARY KEY (order_status_no)
);

INSERT INTO order_status
(
    order_status_no,
    name
) VALUES (
    1,
    '결제완료'
), (
    2,
    '주문취소'
);

-- orders Table Create SQL
CREATE TABLE orders
(
    `order_no`          INT         NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `user_id`           INT         NOT NULL    COMMENT '유저_id',
    `created_at`        DATETIME    NOT NULL    DEFAULT CURRENT_TIMESTAMP COMMENT '생성일시', 
    `is_deleted`        TINYINT     NOT NULL    DEFAULT FALSE COMMENT '삭제여부', 
    PRIMARY KEY (order_no)
);

ALTER TABLE orders
    ADD CONSTRAINT FK_orders_user_id_users_user_no FOREIGN KEY (user_id)
        REFERENCES users (user_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

INSERT INTO orders
(
    order_no,
    user_id,
    created_at
) VALUES (
    1,
    1,
    '2020-08-18 15:00:00'
), (
    2,
    2,
    '2020-08-25 10:00:00'
), (
    3,
    3,
    '2020-07-25 10:00:00'
), (
    4,
    4,
    '2020-05-25 12:30:00'
), (
    5,
    5,
    '2020-05-20 11:20:00'
);

-- sub_categories Table Create SQL
CREATE TABLE sub_categories
(
    `sub_category_no`   INT            NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `main_category_id`  INT            NOT NULL    COMMENT '1차카테고리_id', 
    `name`              VARCHAR(50)    NOT NULL    COMMENT '카테고리명', 
    PRIMARY KEY (sub_category_no)
);

ALTER TABLE sub_categories COMMENT '2차 카테고리';

ALTER TABLE sub_categories
    ADD CONSTRAINT FK_main_category_id FOREIGN KEY (main_category_id)
        REFERENCES main_categories (main_category_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

INSERT INTO sub_categories
(
    sub_category_no,
    name,
    main_category_id
) VALUES (
    1,
    '자켓',
    1
), (
    2,
    '가디건',
    1
), (
    3,
    '코트',
    1
), ( 
    4,
    '점퍼',
    1
), (
    5,
    '패딩',
    1
), (
    6,
    '무스탕/퍼',
    1
), (
    7,
    '기타',
    1
), (
    8,
    '티셔츠',
    2
), (
    9,
    '셔츠/블라우스',
    2
), (
    10,
    '니트',
    2
), (
    11,
    '후드/맨투맨',
    2
), ( 
    12,
    '베스트',
    2
), (
    13,
    '청바지',
    3
), (
    14,
    '슬랙스',
    3
), (
    15, 
    '면바지',
    3
), ( 
    16, 
    '반바지',
    3
), (
    17, 
    '트레이닝/조거',
    3
), (
    18, 
    '레깅스',
    3
), (
    19, 
    '미니',
    4
), (
    20, 
    '미디',
    4
), (
    21, 
    '롱',
    4
), (
    22, 
    '투피스',
    4
), (
    23, 
    '점프수트',
    4
), ( 
    24,
    '미니',
    5
), (
    25, 
    '미디',
    5
), (
    26, 
    '롱',
    5
), (
    27, 
    '플랫/로퍼',
    6
), ( 
    28, 
    '샌들/슬리퍼',
    6
), (
    29, 
    '힐',
    6
), (
    30, 
    '스니커즈',
    6
), (
    31, 
    '부츠/워커',
    6
), (
    32, 
    '크로스백',
    7
), (
    33, 
    '토트백',
    7
), (
    34, 
    '숄더백',
    7
), (
    35, 
    '에코백',
    7
), ( 
    36, 
    '클러치',
    7
), (
    37, 
    '백팩',
    7
), (
    38, 
    '귀걸이',
    8
), (
    39, 
    '목걸이',
    8
), ( 
    40, 
    '팔찌/발찌',
    8
), (
    41, 
    '반지',
    8
), (
    42, 
    '휴대폰 acc',
    9
), (
    43, 
    '헤어 acc',
    9
), (
    44, 
    '양말/스타킹',
    9
), (
    45, 
    '지갑/파우치',
    9
), (
    46, 
    '모자',
    9
), (
    47, 
    '벨트',
    9
), ( 
    48, 
    '시계',
    9
), (
    49, 
    '스카프',
    9
), (
    50, 
    '머플러',
    9
), (
    51, 
    '아이웨어',
    9
), ( 
    52, 
    '기타',
    9
), (
    53, 
    '언더웨어',
    10
), (
    54,
    '홈웨어',
    10
), (
    55, 
    '스윔웨어',
    10
), (
    56, 
    '비치웨어',
    10
), (
    57,
    '기타',
    10
), (
    58, 
    '아우터',
    11
), (
    59, 
    '상의',
    11
), ( 
    60,
    '바지',
    11
), (
    61, 
    '원피스',
    11
), (
    62, 
    '스커트',
    11
);

-- orders_details Table Create SQL
CREATE TABLE orders_details
(
    `order_detail_no`   INT           NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `order_id`          INT           NOT NULL    COMMENT '주문_id', 
    `user_shipping_id`  INT           NOT NULL    COMMENT '배송지_id', 
    `order_status_id`   INT           NOT NULL    COMMENT '주문상태_id', 
    `total_price`       DECIMAL(10,2) NOT NULL    COMMENT '구매할 상품 전체 가격',
    `start_time`        DATETIME      NOT NULL    DEFAULT CURRENT_TIMESTAMP COMMENT '선분이력관리용(생성)', 
    `close_time`        DATETIME      NOT NULL    DEFAULT '9999-12-31 23:59:59'COMMENT '선분이력관리용(삭제)', 
    `delivery_request`  VARCHAR(500)      NULL    COMMENT '배송시 요청사항', 
    PRIMARY KEY (order_detail_no)
);

ALTER TABLE orders_details
    ADD CONSTRAINT FK_user_shipping_id FOREIGN KEY (user_shipping_id)
        REFERENCES user_shipping_details (user_shipping_detail_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE orders_details
    ADD CONSTRAINT FK_order_id FOREIGN KEY (order_id)
        REFERENCES orders (order_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE orders_details
    ADD CONSTRAINT FK_order_status_id FOREIGN KEY (order_status_id)
        REFERENCES order_status (order_status_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

INSERT INTO orders_details
(
    order_detail_no,
    order_id,
    user_shipping_id,
    order_status_id,
    total_price,
    start_time,
    delivery_request
) VALUES (
    1,
    1,
    1,
    1,
    20000,
    '2020-08-18 15:00:00',
    NULL
), (
    2,
    2,
    2,
    1,
    8890,
    '2020-08-25 10:00:00',
    '부재 시 전화주세요'
), (
    3,
    3,
    3,
    1,
    28770,
    '2020-07-25 10:00:00',
    '부재 시 경비실에 맡겨주세요'
), (
    4,
    4,
    4,
    1,
    8820,
    '2020-05-25 12:30:00',
    NULL
), (
    5,
    5,
    5,
    1,
    13230,
    '2020-05-20 11:20:00',
    '부재 시 문앞에 놔주세요'
);

-- images Table Create SQL
CREATE TABLE images
(
    `image_no`      INT             NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `image_large`   VARCHAR(500)    NOT NULL    COMMENT 'Large_이미지_url', 
    `image_medium`  VARCHAR(500)    NOT NULL    COMMENT 'Medium_이미지_url', 
    `image_small`   VARCHAR(500)    NOT NULL    COMMENT 'Small_이미지_url', 
    `is_deleted`    TINYINT         NOT NULL    COMMENT '삭제여부', 
    PRIMARY KEY (image_no)
);

INSERT INTO images
(
    image_no,
    image_large,
    image_medium,
    image_small
) VALUES (
    1,
    "http://image.brandi.me/cproduct/2020/07/06/17993567_1594029654_image2_M.jpg",
    "http://image.brandi.me/cproduct/2020/07/06/17993567_1594029654_image2_M.jpg",
    "http://image.brandi.me/cproduct/2020/07/06/17993567_1594029654_image2_M.jpg"
), (
    2,
    "http://image.brandi.me/cproduct/2020/08/20/16814508_1597899641_image1_M.jpg",
    "http://image.brandi.me/cproduct/2020/08/20/16814508_1597899641_image1_M.jpg",
    "http://image.brandi.me/cproduct/2020/08/20/16814508_1597899641_image1_M.jpg"
), (
    3,
    "http://image.brandi.me/cproduct/2020/05/31/16896246_1590931916_image1_M.jpg",
    "http://image.brandi.me/cproduct/2020/05/31/16896246_1590931916_image1_M.jpg",
    "http://image.brandi.me/cproduct/2020/05/31/16896246_1590931916_image1_M.jpg"
), (
    4,
    "http://image.brandi.me/cproduct/2020/05/29/16841528_1590732351_image1_M.jpg",
    "http://image.brandi.me/cproduct/2020/05/29/16841528_1590732351_image1_M.jpg",
    "http://image.brandi.me/cproduct/2020/05/29/16841528_1590732351_image1_M.jpg"
), (
    5,
    "http://image.brandi.me/cproduct/2020/06/28/17786204_1593354326_image1_M.jpg",
    "http://image.brandi.me/cproduct/2020/06/28/17786204_1593354326_image1_M.jpg",
    "http://image.brandi.me/cproduct/2020/06/28/17786204_1593354326_image1_M.jpg"
), (
    6,
    "http://image.brandi.me/cproduct/2020/06/21/17426352_1592713625_image1_M.jpg",
    "http://image.brandi.me/cproduct/2020/06/21/17426352_1592713625_image1_M.jpg",
    "http://image.brandi.me/cproduct/2020/06/21/17426352_1592713625_image1_M.jpg"
), (
    7,
    "http://image.brandi.me/cproduct/2020/05/18/16379275_1589813844_image1_M.jpg",
    "http://image.brandi.me/cproduct/2020/05/18/16379275_1589813844_image1_M.jpg",
    "http://image.brandi.me/cproduct/2020/05/18/16379275_1589813844_image1_M.jpg"
), (
    8,
    "http://image.brandi.me/cproduct/2020/08/16/18960858_1597566426_image1_M.jpg",
    "http://image.brandi.me/cproduct/2020/08/16/18960858_1597566426_image1_M.jpg",
    "http://image.brandi.me/cproduct/2020/08/16/18960858_1597566426_image1_M.jpg"
), (
    9,
    "http://image.brandi.me/cproduct/2020/05/19/16448262_1589891341_image1_M.jpg",
    "http://image.brandi.me/cproduct/2020/05/19/16448262_1589891341_image1_M.jpg",
    "http://image.brandi.me/cproduct/2020/05/19/16448262_1589891341_image1_M.jpg"
), (
    10,
    "http://image.brandi.me/cproduct/2020/06/08/17184315_1591610586_image1_M.jpg",
    "http://image.brandi.me/cproduct/2020/06/08/17184315_1591610586_image1_M.jpg",
    "http://image.brandi.me/cproduct/2020/06/08/17184315_1591610586_image1_M.jpg"
), (
    11,
    "http://image.brandi.me/cproduct/2020/06/26/17741364_1593101362_image1_M.jpg",
    "http://image.brandi.me/cproduct/2020/06/26/17741364_1593101362_image1_M.jpg",
    "http://image.brandi.me/cproduct/2020/06/26/17741364_1593101362_image1_M.jpg"
), (
    12,
    "http://image.brandi.me/cproduct/2019/08/01/9907221_1564645496_image1_M.jpg",
    "http://image.brandi.me/cproduct/2019/08/01/9907221_1564645496_image1_M.jpg",
    "http://image.brandi.me/cproduct/2019/08/01/9907221_1564645496_image1_M.jpg"
), (
    13,
    "http://image.brandi.me/cproduct/2020/08/10/18846870_1597024374_image1_M.jpg",
    "http://image.brandi.me/cproduct/2020/08/10/18846870_1597024374_image1_M.jpg",
    "http://image.brandi.me/cproduct/2020/08/10/18846870_1597024374_image1_M.jpg"
), (
    14,
    "http://image.brandi.me/cproduct/2020/03/05/5583139_1583400501_image1_M.jpg",
    "http://image.brandi.me/cproduct/2020/03/05/5583139_1583400501_image1_M.jpg",
    "http://image.brandi.me/cproduct/2020/03/05/5583139_1583400501_image1_M.jpg"
), (
    15,
    "http://image.brandi.me/cproduct/2019/08/19/10059176_1566214986_image1_M.jpg",
    "http://image.brandi.me/cproduct/2019/08/19/10059176_1566214986_image1_M.jpg",
    "http://image.brandi.me/cproduct/2019/08/19/10059176_1566214986_image1_M.jpg"
), (
    16,
    "http://image.brandi.me/cproduct/2020/04/28/15899675_1588044782_image1_M.jpg",
    "http://image.brandi.me/cproduct/2020/04/28/15899675_1588044782_image1_M.jpg",
    "http://image.brandi.me/cproduct/2020/04/28/15899675_1588044782_image1_M.jpg"
), (
    17,
    "http://image.brandi.me/cproduct/2020/08/15/18895387_1597493091_image1_M.jpg",
    "http://image.brandi.me/cproduct/2020/08/15/18895387_1597493091_image1_M.jpg",
    "http://image.brandi.me/cproduct/2020/08/15/18895387_1597493091_image1_M.jpg"
), (
    18,
    "http://image.brandi.me/cproduct/2020/04/09/15346962_1586364000_image1_M.jpg",
    "http://image.brandi.me/cproduct/2020/04/09/15346962_1586364000_image1_M.jpg",
    "http://image.brandi.me/cproduct/2020/04/09/15346962_1586364000_image1_M.jpg"
), (
    19,
    "http://image.brandi.me/cproduct/2020/07/10/15153293_1594373068_image1_M.jpg",
    "http://image.brandi.me/cproduct/2020/07/10/15153293_1594373068_image1_M.jpg",
    "http://image.brandi.me/cproduct/2020/07/10/15153293_1594373068_image1_M.jpg"
), (
    20,
    "http://image.brandi.me/cproduct/2020/06/12/17326713_1591894323_image1_M.jpg",
    "http://image.brandi.me/cproduct/2020/06/12/17326713_1591894323_image1_M.jpg",
    "http://image.brandi.me/cproduct/2020/06/12/17326713_1591894323_image1_M.jpg"
), (
    21,
    "https://image.brandi.me/cproduct/2020/07/06/17993567_1594029654_image1_L.jpg",
    "https://image.brandi.me/cproduct/2020/07/06/17993567_1594029654_image1_L.jpg",
    "https://image.brandi.me/cproduct/2020/07/06/17993567_1594029654_image1_L.jpg"
), (
    22,
    "https://image.brandi.me/cproduct/2020/07/06/17993567_1594029656_image5_L.jpg",
    "https://image.brandi.me/cproduct/2020/07/06/17993567_1594029656_image5_L.jpg",
    "https://image.brandi.me/cproduct/2020/07/06/17993567_1594029656_image5_L.jpg"
);

-- product_details Table Create SQL
CREATE TABLE product_details
(
    `product_detail_no`    INT              NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `product_id`           INT              NOT NULL    COMMENT '상품_id', 
    `is_activated`         TINYINT          NOT NULL    COMMENT '판매여부', 
    `is_displayed`         TINYINT          NOT NULL    COMMENT '진열여부', 
    `main_category_id`     INT              NOT NULL    COMMENT '1차카테고리', 
    `sub_category_id`      INT              NOT NULL    COMMENT '2차카테고리', 
    `name`                 VARCHAR(100)     NOT NULL    COMMENT '상품명', 
    `simple_description`   VARCHAR(500)     NULL        COMMENT '한줄 상품 설명', 
    `detail_information`   LONGTEXT         NOT NULL    COMMENT '상품상세정보', 
    `price`                DECIMAL(10,2)    NOT NULL    COMMENT '판매가', 
    `discount_rate`        INT              NULL        COMMENT '할인률', 
    `discount_start_date`  DATETIME         NULL        COMMENT '할인시작일시', 
    `discount_end_date`    DATETIME         NULL        COMMENT '할인종료일시', 
    `min_sales_quantity`   INT              NOT NULL    COMMENT '최소판매수량', 
    `max_sales_quantity`   INT              NOT NULL    COMMENT '최대판매수량', 
    `start_time`           DATETIME         NOT NULL    DEFAULT CURRENT_TIMESTAMP COMMENT '선분이력관리용(생성)', 
    `close_time`           DATETIME         NOT NULL    DEFAULT '9999-12-31 23:59:59' COMMENT '선분이력관리용(삭제)', 
    PRIMARY KEY (product_detail_no)
);

ALTER TABLE product_details
    ADD CONSTRAINT FK_product_details_product_id_products_product_no FOREIGN KEY (product_id)
        REFERENCES products (product_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE product_details
    ADD CONSTRAINT FK_product_details_main_category_id FOREIGN KEY (main_category_id)
        REFERENCES main_categories (main_category_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE product_details
    ADD CONSTRAINT FK_sub_category_id FOREIGN KEY (sub_category_id)
        REFERENCES sub_categories (sub_category_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

INSERT INTO product_details
(
    product_detail_no,
    product_id,
    is_activated,
    is_displayed,
    main_category_id,
    sub_category_id,
    name,
    detail_information,
    price,
    min_sales_quantity,
    max_sales_quantity,
    discount_rate,
    discount_start_date,
    discount_end_date,
    start_time,
    close_time
) VALUES (
    1,
    1,
    1,
    1,
    2,
    8,
    '(요즘대세/여유핏) 카라 반크롭 반팔티(4color)_버튼나인 - 버튼나인',
    '1번 상품 설명',
    10000,
    1,
    20,
    10,
    '2020-04-20 12:00:00',
    '2020-05-20 12:00:00',
    '2020-04-20 12:00:00',
    '2020-08-19 15:00:00'
), (
    2,
    2,
    1,
    1,
    2,
    8,
    '햇빛차단! 여름에도 여리핏 크롭 티셔츠(4color)_버튼나인 - 버튼나인',
    '2번 상품 설명',
    11110,
    1,
    20,
    20,
    NULL,
    NULL,
    '2020-04-20 12:00:00',
    DEFAULT
), (
    3,
    3,
    1,
    1,
    2,
    8,
    '(6col/린넨) 썸머 린넨 루즈 니트 티셔츠_반하리마켓 - 반하리마켓',
    '3번 상품 설명',
    13700,
    1,
    20,
    30,
    '2020-04-20 15:00:00',
    '2021-04-20 15:00:00',
    '2020-04-20 12:00:00',
    DEFAULT
), (
    4,
    4,
    1,
    1,
    2,
    8,
    '(여유핏) 데일리로딱! 반크롭 반팔티(8color)_버튼나인 - 버튼나인',
    '4번 상품 설명',
    8820,
    1,
    20,
    NULL,
    NULL,
    NULL,
    '2020-04-20 12:00:00',
    DEFAULT
), (
    5,
    5,
    1,
    1,
    2,
    9,
    '박시핏 여리여리 여름셔츠 시스루 남방_블리즈 - 블리즈',
    '5번 상품 설명',
    13230,
    1,
    20,
    NULL,
    NULL,
    NULL,
    '2020-04-20 12:00:00',
    DEFAULT
), (
    6,
    6,
    1,
    1,
    2,
    9,
    '린넨 슈 스퀘어 반팔 블라우스 (4 color)_로그인 - 로그인',
    '6번 상품 설명',
    14700,
    1,
    20,
    10,
    NULL,
    NULL,
    '2020-04-20 12:00:00',
    DEFAULT
), (
    7,
    7,
    0,
    1,
    2,
    9,
    '르메 여름 파스텔 카라 베이직 카라 루즈핏 반팔 셔츠_프렌치오브 - 프렌치오브',
    '7번 상품 설명',
    13230,
    1,
    20,
    20,
    '2020-08-20 13:00:00',
    '2020-09-04 15:00:00',
    '2020-04-20 12:00:00',
    DEFAULT
), (
    8,
    8,
    1,
    1,
    2,
    9,
    '강추 리본블라우스 가을블라우스 4col_무드글램 - 무드글램',
    '8번 상품 설명',
    16100,
    1,
    20,
    30,
    '2020-09-04 00:00:00',
    '2020-10-04 00:00:00',
    '2020-04-20 12:00:00',
    DEFAULT
), (
    9,
    9,
    1,
    1,
    2,
    10,
    '(활용도굿!!) 루즈핏 레이어드 여리핏 시스루 니트 / 시스루티셔츠 / 여름니트 [6color]_오프닝무드 - 오프닝무드',
    '9번 상품 설명',
    9800,
    1,
    20,
    NULL,
    NULL,
    NULL,
    '2020-04-20 12:00:00',
    DEFAULT
), (
    10,
    10,
    1,
    1,
    2,
    10,
    '브이골지티_모던제이 - 모던제이',
    '10번 상품 설명',
    14700,
    1,
    20,
    10,
    '2020-10-05 13:00:00',
    '2020-10-05 14:00:00',
    '2020-04-20 12:00:00',
    DEFAULT
), (
    11,
    11,
    1,
    0,
    2,
    10,
    '(6col)민자 보트넥 썸머 여리 긴팔 니트 티셔츠_반하리마켓 - 반하리마켓',
    '11번 상품 설명',
    13960,
    1,
    20,
    20,
    '2020-09-05 15:00:00',
    '2020-10-05 15:00:00',
    '2020-04-20 12:00:00',
    DEFAULT
), (
    12,
    12,
    1,
    1,
    2,
    10,
    '[여리여리핏♥V넥NT]버츠 부클 브이니트 - 헤이레이디',
    '12번 상품 설명',
    14900,
    1,
    20,
    30,
    NULL,
    NULL,
    '2020-04-20 12:00:00',
    DEFAULT
), (
    13,
    13,
    1,
    1,
    2,
    11,
    '조슈아 코튼 맨투맨 - 어반로지',
    '13번 상품 설명',
    26500,
    1,
    20,
    NULL,
    NULL,
    NULL,
    '2020-04-20 12:00:00',
    DEFAULT
), (
    14,
    14,
    0,
    0,
    2,
    11,
    '양기모 오버 패치 맨투맨 (5color)_모어데이 - 모어데이',
    '14번 상품 설명',
    18900,
    1,
    20,
    10,
    '2020-04-20 12:00:00',
    '2020-09-05 12:00:00',
    '2020-04-20 12:00:00',
    DEFAULT
), (
    15,
    15,
    1,
    1,
    2,
    11,
    '(무료배송)풀 박시핏 워싱 피그먼트 맨투맨 - 링거인무드',
    '15번 상품 설명',
    34200,
    1,
    20,
    20,
    NULL,
    NULL,
    '2020-04-20 12:00:00',
    DEFAULT
), (
    16,
    16,
    1,
    1,
    2,
    11,
    '★최저가★ 윈드 아노락세트 / 후드+반바지세트 4color_밀리 - 밀리',
    '16번 상품 설명',
    29520,
    1,
    20,
    30,
    '2020-09-01 00:00:00',
    '2020-09-10 00;00:00',
    '2020-04-20 12:00:00',
    DEFAULT
), (
    17,
    17,
    1,
    1,
    2,
    12,
    '[인기]유니크골지니트조끼(4color) - 꼬맹',
    '17번 상품 설명',
    12900,
    1,
    20,
    NULL,
    NULL,
    NULL,
    '2020-04-20 12:00:00',
    DEFAULT
), (
    18,
    18,
    1,
    1,
    2,
    12,
    '브이넥 니트 조끼 베스트 2color - 핀더패브릭',
    '18번 상품 설명',
    25730,
    1,
    20,
    10,
    NULL,
    NULL,
    '2020-04-20 12:00:00',
    DEFAULT
), (
    19,
    19,
    1,
    1,
    2,
    12,
    '♥판매율1위♥클라우드 니트 베스트 (4color) - 스퀘어101',
    '19번 상품 설명',
    12780,
    1,
    20,
    20,
    NULL,
    NULL,
    '2020-04-20 12:00:00',
    DEFAULT
), (
    20,
    20,
    1,
    1,
    2,
    12,
    '플레어 나시 블라우스 (4color)_더모닌 - 더모닌',
    '20번 상품 설명',
    14700,
    1,
    20,
    NULL,
    NULL,
    NULL,
    '2020-04-20 12:00:00',
    DEFAULT
), (
    21,
    1,
    1,
    1,
    2,
    8,
    '선분이력테스트 (요즘대세/여유핏) 카라 반크롭 반팔티(4color)_버튼나인 - 버튼나인',
    '1번 상품 설명 선분이력테스트',
    11250,
    1,
    20,
    30,
    '2020-08-19 16:00:00',
    '2020-09-15 16:00:00',
    '2020-08-19 15:00:00',
    DEFAULT
);

-- product_images Table Create SQL
CREATE TABLE product_images
(
    `product_image_no`  INT         NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `product_id`        INT         NOT NULL    COMMENT '상품상세_id', 
    `image_id`          INT         NOT NULL    COMMENT '이미지_id', 
    `is_main`           TINYINT     NOT NULL    DEFAULT FALSE COMMENT '대표이미지여부', 
    `start_time`        DATETIME    NOT NULL    DEFAULT CURRENT_TIMESTAMP COMMENT '선분이력관리(생성)', 
    `close_time`        DATETIME    NOT NULL    DEFAULT '9999-12-31 23:59:59' COMMENT '선분이력관리(삭제)', 
    PRIMARY KEY (product_image_no)
);

ALTER TABLE product_images COMMENT '상품이미지';

ALTER TABLE product_images
    ADD CONSTRAINT FK_product_images_product_id FOREIGN KEY (product_id)
        REFERENCES products (product_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE product_images
    ADD CONSTRAINT FK_image_id FOREIGN KEY (image_id)
        REFERENCES images (image_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

INSERT INTO product_images
(
    product_image_no,
    product_id,
    image_id,
    is_main,
    start_time,
    close_time
) VALUES (
    1,
    1,
    1,
    1,
    '2020-03-20 13:00:00',
    CURRENT_TIMESTAMP
), (
    2,
    2,
    2,
    1,
    '2020-03-20 13:00:00',
    DEFAULT
), (
    3,
    3,
    3,
    1,
    '2020-03-20 13:00:00',
    DEFAULT
), (
    4,
    4,
    4,
    1,
    '2020-03-20 13:00:00',
    DEFAULT
), (
    5,
    5,
    5,
    1,
    '2020-03-20 13:00:00',
    DEFAULT
), (
    6,
    6,
    6,
    1,
    '2020-03-20 13:00:00',
    DEFAULT
), (
    7,
    7,
    7,
    1,
    '2020-03-20 13:00:00',
    DEFAULT
), (
    8,
    8,
    8,
    1,
    '2020-03-20 13:00:00',
    DEFAULT
), (
    9,
    9,
    9,
    1,
    '2020-03-20 13:00:00',
    DEFAULT
), (
    10,
    10,
    10,
    1,
    '2020-03-20 13:00:00',
    DEFAULT
), (
    11,
    11,
    11,
    1,
    '2020-03-20 13:00:00',
    DEFAULT
), (
    12,
    12,
    12,
    1,
    '2020-03-20 13:00:00',
    DEFAULT
), (
    13,
    13,
    13,
    1,
    '2020-03-20 13:00:00',
    DEFAULT
), (
    14,
    14,
    14,
    1,
    '2020-03-20 13:00:00',
    DEFAULT
), (
    15,
    15,
    15,
    1,
    '2020-03-20 13:00:00',
    DEFAULT
), (
    16,
    16,
    16,
    1,
    '2020-03-20 13:00:00',
    DEFAULT
), (
    17,
    17,
    17,
    1,
    '2020-03-20 13:00:00',
    DEFAULT
), (
    18,
    18,
    18,
    1,
    '2020-03-20 13:00:00',
    DEFAULT
), (
    19,
    19,
    19,
    1,
    '2020-03-20 13:00:00',
    DEFAULT
), (
    20,
    20,
    20,
    1,
    '2020-03-20 13:00:00',
    DEFAULT
), (
    21,
    1,
    21,
    0,
    '2020-03-20 13:00:00',
    DEFAULT
), (
    22,
    1,
    22,
    1,
    CURRENT_TIMESTAMP,
    DEFAULT
);

-- order_product Table Create SQL
CREATE TABLE order_product
(
    `order_product_no`   INT    NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `order_detail_id`    INT    NOT NULL    COMMENT '주문상세_id', 
    `product_option_id`  INT    NOT NULL    COMMENT '상품상세_id', 
    `quantity`           INT    NOT NULL    COMMENT '주문수량', 
    PRIMARY KEY (order_product_no)
);

ALTER TABLE order_product
    ADD CONSTRAINT FK_order_product_order_detail_id FOREIGN KEY (order_detail_id)
        REFERENCES orders_details (order_detail_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE order_product
    ADD CONSTRAINT FK_order_product_product_option_id FOREIGN KEY (product_option_id)
        REFERENCES product_options (product_option_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

INSERT INTO order_product
(
    order_product_no,
    order_detail_id,
    product_option_id,
    quantity
) VALUES (
    1,
    1,
    1,
    2
), (
    2,
    2,
    2,
    1
), (
    3,
    3,
    3,
    3
), (
    4,
    4,
    4,
    1
), (
    5,
    5,
    5,
    1
);

-- quantities Table Create SQL
CREATE TABLE quantities
(
    `quantity_no`        INT         NOT NULL    AUTO_INCREMENT COMMENT 'pk', 
    `product_option_id`  INT         NOT NULL    COMMENT '상품_옵션_id', 
    `quantity`           INT         NOT NULL    COMMENT '재고', 
    `start_time`         DATETIME    NOT NULL    DEFAULT CURRENT_TIMESTAMP COMMENT '선분이력관리용(생성)', 
    `close_time`         DATETIME    NOT NULL    DEFAULT '9999-12-31 23:59:59' COMMENT '선분이력관리용(삭제)', 
    PRIMARY KEY (quantity_no)
);

ALTER TABLE quantities
    ADD CONSTRAINT FK_product_option_id FOREIGN KEY (product_option_id)
        REFERENCES product_options (product_option_no) ON DELETE RESTRICT ON UPDATE RESTRICT;

INSERT INTO quantities
(
    quantity_no,
    product_option_id,
    quantity
) VALUES (
    1,
    1,
    30
), (
    2,
    2,
    40
), (
    3,
    3,
    50
), (
    4,
    4,
    100
), (
    5,
    5,
    150
), (
    6,
    6,
    150
), (
    7,
    7,
    150
), (
    8,
    8,
    2000
), (
    9,
    9,
    150
), (
    10,
    10,
    1500
), (
    11,
    11,
    1300
), (
    12,
    12,
    46
), (
    13,
    13,
    17
), (
    14,
    14,
    13
), (
    15,
    15,
    100
), (
    16,
    16,
    1234
), (
    17,
    17,
    345
), (
    18,
    18,
    856
), (
    19,
    19,
    935
), (
    20,
    20,
    375
), (
    21,
    21,
    12
), (
    22,
    22,
    1212
), (
    23,
    23,
    3000
), (
    24,
    24,
    300
), (
    25,
    25,
    77
), (
    26,
    26,
    150
), (
    27,
    27,
    99
), (
    28,
    28,
    20
);
