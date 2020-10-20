const car_types = [{
    id: 1,
    brand: 'TOYOTA',
    jp_name: 'カローラ',
    jp_hira: 'かろーら',
    en_name: 'Corolla',
    images: 'https://toyota.jp/pages/contents/corollasport/001_p_001/4.0/image/car-viewer/43_1_5/43_1_5_030_c.jpg'
  },
  {
    id: 2,
    brand: 'TOYOTA',
    jp_name: 'プリウス',
    jp_hira: 'ぷりうす',
    en_name: 'Prius',
    images: 'https://toyota.jp/pages/contents/prius/004_p_007/4.0/image/car-viewer/24_5_7/24_5_7_030_c.jpg'
  },
  {
    id: 3,
    brand: 'TOYOTA',
    jp_name: 'ヴォクシー',
    jp_hira: 'ゔぉくしー',
    en_name: 'Voxy',
    images: 'https://toyota.jp/pages/contents/voxy/003_p_007/4.0/image/car-viewer/11_1_1/11_1_1_030_c.jpg'
  },
  {
    id: 4,
    brand: 'TOYOTA',
    jp_name: 'シエンタ',
    jp_hira: 'しえんた',
    en_name: 'Sienta',
    images: 'https://toyota.jp/pages/contents/sienta/002_p_003/4.0/image/car-viewer/15_24_2/15_24_2_030_c.jpg'
  },
  {
    id: 5,
    brand: 'TOYOTA',
    jp_name: 'アクア',
    jp_hira: 'あくあ',
    en_name: 'AQUA',
    images: 'https://toyota.jp/pages/contents/aqua/001_p_011/4.0/image/car-viewer/1_6_9/1_6_9_030_c.jpg'
  },
  {
    id: 6,
    brand: 'TOYOTA',
    jp_name: 'アルファード',
    jp_hira: 'あるふぁーど',
    en_name: 'ALPHARD',
    images: 'https://toyota.jp/pages/contents/alphard/003_p_009/image/car-viewer/9_20_6/9_20_6_030_c.jpg'
  },
  {
    id: 7,
    brand: 'HONDA',
    jp_name: 'フィット',
    jp_hira: 'ふぃっと',
    en_name: 'FIT',
    images: 'https://www.honda.co.jp/Fit/webcatalog/type/type/image/ehev_home/bc_sunlight_white.jpg'
  },
  {
    id: 8,
    brand: 'HONDA',
    jp_name: 'シャトル',
    jp_hira: 'しゃとる',
    en_name: 'SHUTTLE',
    images: 'https://img1.kakaku.k-img.com/images/productimage/fullscale/K0000770924.jpg'
  },
  {
    id: 9,
    brand: 'HONDA',
    jp_name: 'ステップワゴン',
    jp_hira: 'すてっぷわごん',
    en_name: 'STEP WGN',
    images: 'https://car.watch.impress.co.jp/img/car/docs/1159/425/012_l.jpg'
  },
  {
    id: 10,
    brand: 'HONDA',
    jp_name: 'インサイト',
    jp_hira: 'いんさいと',
    en_name: 'INSIGHT',
    images: 'https://lh3.googleusercontent.com/proxy/_Pj52zDm-a0UB3xqkDdNsTVDj0MnLkzt7S3_mhO-Aqwl7DT-OL-r5AQnqVrmCnKLEv5szxYK_EUPD0hkNrqj9VQ5P2HKrGnI8RT8YQrHPEqpL7Z6sD5E6Pv5iECt7M41bHzVEPgIFZmxE-FxznoVulgY5fhExieFTIa_'
  },
  {
    id: 11,
    brand: 'HONDA',
    jp_name: 'N-BOX',
    jp_hira: 'えぬぼっくす',
    en_name: 'N-BOX',
    images: 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTwrPlYshaUlXOm_PGqpJgzaTOAlbwUE3aT2A&usqp=CAU'
  },
  {
    id: 12,
    brand: 'HONDA',
    jp_name: 'N-WGN',
    jp_hira: 'えぬワゴン',
    en_name: 'N-WGN',
    images: 'https://www.honda.co.jp/N-WGN/webcatalog/type/type/image/std_l/bc_crystal_black.jpg'
  },
  {
    id: 13,
    brand: 'MAZDA',
    jp_name: 'MAZDA2',
    jp_hira: 'まつだつー',
    en_name: 'MAZDA2',
    images: 'https://www.mazda.co.jp/globalassets/assets/cars/mazda2/mazda2/dj2/common/default_s.png'
  },
  {
    id: 14,
    brand: 'MAZDA',
    jp_name: 'MAZDA3',
    jp_hira: 'まつだすりー',
    en_name: 'MAZDA3',
    images: 'https://www.mazda.co.jp/globalassets/assets/cars/mazda3/mazda3-fastback/bp2/common/default_s.png'
  },
  {
    id: 15,
    brand: 'MAZDA',
    jp_name: 'MAZDA6',
    jp_hira: 'まつだしっくす',
    en_name: 'MAZDA6',
    images: 'https://www.mazda.co.jp/globalassets/assets/cars/mazda6/mazda6-wagon/aw2/common/default_s.png'
  },
  {
    id: 16,
    brand: 'MAZDA',
    jp_name: 'MAZDA CX-5',
    jp_hira: 'まつだしーえっくすふぁいぶ',
    en_name: 'MAZDA CX-5',
    images: 'https://www.mazda.co.jp/globalassets/assets/cars/cx-5/cx-5/kf6/common/default_s.png'
  },
  {
    id: 17,
    brand: 'MAZDA',
    jp_name: 'MAZDA CX-8',
    jp_hira: 'まつだしーえっくすえいと',
    en_name: 'MAZDA CX-8',
    images: 'https://www.mazda.co.jp/globalassets/assets/cars/cx-8/cx-8/gk3/common/default_s.png'
  },
  {
    id: 18,
    brand: 'MAZDA',
    jp_name: 'MAZDA CX-30',
    jp_hira: 'まつだしーえっくすさーてぃー',
    en_name: 'MAZDA CX-30',
    images: 'https://www.mazda.co.jp/globalassets/assets/cars/mx-30/mx-30/dr1/common/default_s.png'
  },
]

export default car_types;