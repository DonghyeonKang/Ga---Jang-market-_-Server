CREATE TABLE market(
    id INT PRIMARY KEY AUTO_INCREMENT,
    market_name TEXT NOT NULL,
    market_region TEXT NOT NULL,
    market_address TEXT NOT NULL,
    info TEXT NOT NULL,
    latitude DECIMAL(25,20) NOT NULL,
    longitude DECIMAL(25,20) NOT NULL
);

CREATE TABLE market_img(
    m_id INT NOT NULL,
    img_path TEXT NOT NULL,
    FOREIGN KEY (`m_id`) REFERENCES `market` (`id`) ON DELETE CASCADE
);

-- store type 은 0이면 상시, 1이면 일일 매장
CREATE TABLE store(
    id INT PRIMARY KEY AUTO_INCREMENT,
    m_id INT NOT NULL,
    store_name TEXT NOT NULL,
    info TEXT NOT NULL,
    store_type INT NOT NULL,
    open_time TIME NOT NULL,
    close_time TIME NOT NULL,
    latitude DECIMAL(25,20),
    longitude DECIMAL(25,20),
    FOREIGN KEY (`m_id`) REFERENCES `market` (`id`) ON DELETE CASCADE
);

CREATE TABLE store_img(
    s_id INT NOT NULL,
    img_path TEXT NOT NULL,
    FOREIGN KEY (`s_id`) REFERENCES `store` (`id`) ON DELETE CASCADE
);

CREATE TABLE product(
    id INT PRIMARY KEY AUTO_INCREMENT,
    s_id INT NOT NULL,
    product_name TEXT NOT NULL,
    FOREIGN KEY (`s_id`) REFERENCES `store` (`id`) ON DELETE CASCADE
);

CREATE TABLE product_selling_option(
    p_id INT NOT NULL,
    price INT NOT NULL,
    selling_option TEXT,
    FOREIGN KEY (`p_id`) REFERENCES `product` (`id`) ON DELETE CASCADE

);

CREATE TABLE product_img(
    p_id INT NOT NULL,
    s_id INT NOT NULL,
    img_path TEXT NOT NULL,
    FOREIGN KEY (`p_id`) REFERENCES `product` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`s_id`) REFERENCES `store` (`id`) ON DELETE CASCADE
);

CREATE TABLE users_customer(
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id TEXT NOT NULL,
    user_pw TEXT NOT NULL
);

CREATE TABLE users_merchant(
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id TEXT NOT NULL,
    user_pw TEXT NOT NULL
);

CREATE TABLE favorites_store(
    uc_id INT NOT NULL,
    s_id INT NOT NULL,
    FOREIGN KEY (`uc_id`) REFERENCES `users_customer` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`s_id`) REFERENCES `store` (`id`) ON DELETE CASCADE
);

CREATE TABLE favorites_product(
    uc_id INT NOT NULL,
    p_id INT NOT NULL,
    FOREIGN KEY (`uc_id`) REFERENCES `users_customer` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`p_id`) REFERENCES `product` (`id`) ON DELETE CASCADE
);

CREATE TABLE management(
    um_id INT NOT NULL,
    s_id INT NOT NULL,
    FOREIGN KEY (`um_id`) REFERENCES `users_merchant` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`s_id`) REFERENCES `store` (`id`) ON DELETE CASCADE
);

CREATE TABLE reservation(
    id INT PRIMARY KEY AUTO_INCREMENT,
    uc_id INT NOT NULL,
    um_id INT NOT NULL,
    p_id INT NOT NULL,
    s_id INT NOT NULL,
    reservation_time TIME NOT NULL,
    price INT NOT NULL,
    count INT NOT NULL,
    approval INT NOT NULL,
    FOREIGN KEY (`uc_id`) REFERENCES `users_customer` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`um_id`) REFERENCES `users_merchant` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`p_id`) REFERENCES `product` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`s_id`) REFERENCES `store` (`id`) ON DELETE CASCADE
);

CREATE TABLE token(
    user_id TEXT NOT NULL,
    refresh_token TEXT NOT NULL
);