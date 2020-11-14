const posts = [
  {
    id: 1,
    user_info: [
      {
      name: 'よしぴー',
      pr: '車好きの中でも車を愛している方です！いつも車内を綺麗に掃除するのが日課になってます。笑 ぜひ、僕の愛車で旅行などを楽しんでもらえたら嬉しいです！ご質問あれば連絡くださいね。',
      icon: 'https://img.icons8.com/color/452/batman.png'
      }
    ],
    address: '福岡県福岡市博多区博多駅前',
    main_images: [
      {
        photo: 'https://response.jp/imgs/thumb_h2/1368463.jpg',
      },
      {
        photo: 'https://toyota.jp/pages/contents/prius/004_p_007/4.0/image/top_design_ext.jpg',
      },
      {
        photo: 'https://motor-fan.jp/images/articles/10006723/big_main10006723_20181128205859000000.png',
      },
      {
        photo: 'https://toyota.jp/pages/contents/prius/004_p_007/4.0/image/top_conductor_perf.jpg',
      }
    ],
    car_info: [
      {
        infomation: '満タン時の走行距離：20km',
      },
      {
        infomation: '駆動方式：2WD',
      },
      {
        infomation: '色：ホワイト',
      },
      {
        infomation: 'エンジン：ガソリン',
      },
      {
        infomation: '定員数：5名',
      },
    ],
    car_recommend1: [
      {
        point: '24h貸し出しOK',
      },
      {
        point: 'アメニティ・設備が豊富',
      },
      {
        point: 'クルーズコントロールでエコ運転',
      },
      {
        point: '定員数：5名',
      },
    ],
    car_recommend2: [
      {
      point: 'まだ買ったばかりなので、かなり綺麗な方だと思います。運転席は結構広いのでひざを伸ばしても座ることができますよ。後部座席も乗ってみると意外と広いと思います！'
    }],
    car_recommend3: [
      {
      point: '後ろの席も結構広いのでゴルフバックなら3つほど入るような感じです。'
      }
    ],
    pr1: '24h貸し出し可能',
    pr2: 'クルーズコントロール、カーナビ、TOYOTAセーフティ機能付',
    pr3: 'TOYOTAセーフティ機能付',
    pr4: '定員5人OK',
    tag1: '1ヶ月間貸し出しOK',
    tag2: '駐車場無料使用OK',
    price: '8,700',
    car_type: 'prius',
    title: 'プリウスの歴史・概要',
    text: 'プリウスの登場は、2001年だ。センタータンクレイアウトを採用し、広大な室内スペースと低燃費性能を実現したモデルとして誕生した。',
  },
  {
    id: 2,
    user_info: [
      {
      name: 'よしぴー',
      pr: '車好きの中でも車を愛している方です！いつも車内を綺麗に掃除するのが日課になってます。笑 ぜひ、僕の愛車で旅行などを楽しんでもらえたら嬉しいです！ご質問あれば連絡くださいね。',
      icon: 'https://img.icons8.com/color/452/batman.png'
      }
    ],
    address: '福岡県福岡市博多区博多駅前',
    main_images: [
      {
        photo: 'https://response.jp/imgs/thumb_h2/1368463.jpg',
      },
      {
        photo: 'https://toyota.jp/pages/contents/prius/004_p_007/4.0/image/top_design_ext.jpg',
      },
      {
        photo: 'https://motor-fan.jp/images/articles/10006723/big_main10006723_20181128205859000000.png',
      },
      {
        photo: 'https://toyota.jp/pages/contents/prius/004_p_007/4.0/image/top_conductor_perf.jpg',
      }
    ],
    car_info: [
      {
        infomation: '満タン時の走行距離：20km',
      },
      {
        infomation: '駆動方式：2WD',
      },
      {
        infomation: '色：ホワイト',
      },
      {
        infomation: 'エンジン：ガソリン',
      },
      {
        infomation: '定員数：5名',
      },
    ],
    car_recommend1: [
      {
        point: '24h貸し出しOK',
      },
      {
        point: 'アメニティ・設備が豊富',
      },
      {
        point: 'クルーズコントロールでエコ運転',
      },
      {
        point: '定員数：5名',
      },
    ],
    car_recommend2: [
      {
      point: 'まだ買ったばかりなので、かなり綺麗な方だと思います。運転席は結構広いのでひざを伸ばしても座ることができますよ。後部座席も乗ってみると意外と広いと思います！'
      }
    ],
    car_recommend3: [
      {
      point: '後ろの席も結構広いのでゴルフバックなら3つほど入るような感じです。'
    }
    ],
    pr1: '24h貸し出し可能',
    pr2: 'クルーズコントロール、カーナビ、TOYOTAセーフティ機能付',
    pr3: 'TOYOTAセーフティ機能付',
    pr4: '定員5人OK',
    tag1: '1ヶ月間貸し出しOK',
    tag2: '駐車場無料使用OK',
    price: '8,700',
    car_type: 'corolla',
    title: 'プリウスの歴史・概要',
    text: 'プリウスの登場は、2001年だ。センタータンクレイアウトを採用し、広大な室内スペースと低燃費性能を実現したモデルとして誕生した。',
  },
  {
    id: 3,
    user_info: [
      {
      name: 'よしぴー',
      pr: '車好きの中でも車を愛している方です！いつも車内を綺麗に掃除するのが日課になってます。笑 ぜひ、僕の愛車で旅行などを楽しんでもらえたら嬉しいです！ご質問あれば連絡くださいね。',
      icon: 'https://img.icons8.com/color/452/batman.png'
      }
    ],
    address: '福岡県福岡市博多区博多駅前',
    main_images: [
      {
        photo: 'https://response.jp/imgs/thumb_h2/1368463.jpg',
      },
      {
        photo: 'https://toyota.jp/pages/contents/prius/004_p_007/4.0/image/top_design_ext.jpg',
      },
      {
        photo: 'https://motor-fan.jp/images/articles/10006723/big_main10006723_20181128205859000000.png',
      },
      {
        photo: 'https://toyota.jp/pages/contents/prius/004_p_007/4.0/image/top_conductor_perf.jpg',
      }
    ],
    car_info: [
      {
        infomation: '満タン時の走行距離：20km',
      },
      {
        infomation: '駆動方式：2WD',
      },
      {
        infomation: '色：ホワイト',
      },
      {
        infomation: 'エンジン：ガソリン',
      },
      {
        infomation: '定員数：5名',
      },
    ],
    car_recommend1: [
      {
        point: '24h貸し出しOK',
      },
      {
        point: 'アメニティ・設備が豊富',
      },
      {
        point: 'クルーズコントロールでエコ運転',
      },
      {
        point: '定員数：5名',
      },
    ],
    car_recommend2: [
      {
      point: 'まだ買ったばかりなので、かなり綺麗な方だと思います。運転席は結構広いのでひざを伸ばしても座ることができますよ。後部座席も乗ってみると意外と広いと思います！'
      }
    ],
    car_recommend3: [
      {
      point: '後ろの席も結構広いのでゴルフバックなら3つほど入るような感じです。'
      }
    ],
    pr1: '24h貸し出し可能',
    pr2: 'クルーズコントロール、カーナビ、TOYOTAセーフティ機能付',
    pr3: 'TOYOTAセーフティ機能付',
    pr4: '定員5人OK',
    tag1: '1ヶ月間貸し出しOK',
    tag2: '駐車場無料使用OK',
    price: '8,700',
    car_type: 'corolla',
    title: 'プリウスの歴史・概要',
    text: 'プリウスの登場は、2001年だ。センタータンクレイアウトを採用し、広大な室内スペースと低燃費性能を実現したモデルとして誕生した。',
  },
  {
    id: 4,
    user_info: [
      {
      name: 'よしぴー',
      pr: '車好きの中でも車を愛している方です！いつも車内を綺麗に掃除するのが日課になってます。笑 ぜひ、僕の愛車で旅行などを楽しんでもらえたら嬉しいです！ご質問あれば連絡くださいね。',
      icon: 'https://img.icons8.com/color/452/batman.png'
      }
    ],
    address: '福岡県福岡市博多区博多駅前',
    main_images: [
      {
        photo: 'https://response.jp/imgs/thumb_h2/1368463.jpg',
      },
      {
        photo: 'https://toyota.jp/pages/contents/prius/004_p_007/4.0/image/top_design_ext.jpg',
      },
      {
        photo: 'https://motor-fan.jp/images/articles/10006723/big_main10006723_20181128205859000000.png',
      },
      {
        photo: 'https://toyota.jp/pages/contents/prius/004_p_007/4.0/image/top_conductor_perf.jpg',
      }
    ],
    car_info: [
      {
        infomation: '満タン時の走行距離：20km',
      },
      {
        infomation: '駆動方式：2WD',
      },
      {
        infomation: '色：ホワイト',
      },
      {
        infomation: 'エンジン：ガソリン',
      },
      {
        infomation: '定員数：5名',
      },
    ],
    car_recommend1: [
      {
        point: '24h貸し出しOK',
      },
      {
        point: 'アメニティ・設備が豊富',
      },
      {
        point: 'クルーズコントロールでエコ運転',
      },
      {
        point: '定員数：5名',
      },
    ],
    car_recommend2: [
      {
      point: 'まだ買ったばかりなので、かなり綺麗な方だと思います。運転席は結構広いのでひざを伸ばしても座ることができますよ。後部座席も乗ってみると意外と広いと思います！'
      }
    ],
    car_recommend3: [
      {
      point: '後ろの席も結構広いのでゴルフバックなら3つほど入るような感じです。'
      }
    ],
    pr1: '24h貸し出し可能',
    pr2: 'クルーズコントロール、カーナビ、TOYOTAセーフティ機能付',
    pr3: 'TOYOTAセーフティ機能付',
    pr4: '定員5人OK',
    tag1: '1ヶ月間貸し出しOK',
    tag2: '駐車場無料使用OK',
    price: '8,700',
    car_type: 'prius',
    title: 'プリウスの歴史・概要',
    text: 'プリウスの登場は、2001年だ。センタータンクレイアウトを採用し、広大な室内スペースと低燃費性能を実現したモデルとして誕生した。',
  },
  {
    id: 5,
    user_info: [
      {
      name: 'よしぴー',
      pr: '車好きの中でも車を愛している方です！いつも車内を綺麗に掃除するのが日課になってます。笑 ぜひ、僕の愛車で旅行などを楽しんでもらえたら嬉しいです！ご質問あれば連絡くださいね。',
      icon: 'https://img.icons8.com/color/452/batman.png'
      }
    ],
    address: '福岡県福岡市博多区博多駅前',
    main_images: [
      {
        photo: 'https://response.jp/imgs/thumb_h2/1368463.jpg',
      },
      {
        photo: 'https://toyota.jp/pages/contents/prius/004_p_007/4.0/image/top_design_ext.jpg',
      },
      {
        photo: 'https://motor-fan.jp/images/articles/10006723/big_main10006723_20181128205859000000.png',
      },
      {
        photo: 'https://toyota.jp/pages/contents/prius/004_p_007/4.0/image/top_conductor_perf.jpg',
      }
    ],
    car_info: [
      {
        infomation: '満タン時の走行距離：20km',
      },
      {
        infomation: '駆動方式：2WD',
      },
      {
        infomation: '色：ホワイト',
      },
      {
        infomation: 'エンジン：ガソリン',
      },
      {
        infomation: '定員数：5名',
      },
    ],
    car_recommend1: [
      {
        point: '24h貸し出しOK',
      },
      {
        point: 'アメニティ・設備が豊富',
      },
      {
        point: 'クルーズコントロールでエコ運転',
      },
      {
        point: '定員数：5名',
      },
    ],
    car_recommend2: [
      {
      point: 'まだ買ったばかりなので、かなり綺麗な方だと思います。運転席は結構広いのでひざを伸ばしても座ることができますよ。後部座席も乗ってみると意外と広いと思います！'
      }
    ],
    car_recommend3: [
      {
      point: '後ろの席も結構広いのでゴルフバックなら3つほど入るような感じです。'
      }
    ],
    pr1: '24h貸し出し可能',
    pr2: 'クルーズコントロール、カーナビ、TOYOTAセーフティ機能付',
    pr3: 'TOYOTAセーフティ機能付',
    pr4: '定員5人OK',
    tag1: '1ヶ月間貸し出しOK',
    tag2: '駐車場無料使用OK',
    price: '8,700',
    car_type: 'corolla',
    title: 'プリウスの歴史・概要',
    text: 'プリウスの登場は、2001年だ。センタータンクレイアウトを採用し、広大な室内スペースと低燃費性能を実現したモデルとして誕生した。',
  },
  {
    id: 6,
    user_info: [
      {
      name: 'よしぴー',
      pr: '車好きの中でも車を愛している方です！いつも車内を綺麗に掃除するのが日課になってます。笑 ぜひ、僕の愛車で旅行などを楽しんでもらえたら嬉しいです！ご質問あれば連絡くださいね。',
      icon: 'https://img.icons8.com/color/452/batman.png'
      }
    ],
    address: '福岡県福岡市博多区博多駅前',
    main_images: [
      {
        photo: 'https://response.jp/imgs/thumb_h2/1368463.jpg',
      },
      {
        photo: 'https://toyota.jp/pages/contents/prius/004_p_007/4.0/image/top_design_ext.jpg',
      },
      {
        photo: 'https://motor-fan.jp/images/articles/10006723/big_main10006723_20181128205859000000.png',
      },
      {
        photo: 'https://toyota.jp/pages/contents/prius/004_p_007/4.0/image/top_conductor_perf.jpg',
      }
    ],
    car_info: [
      {
        infomation: '満タン時の走行距離：20km',
      },
      {
        infomation: '駆動方式：2WD',
      },
      {
        infomation: '色：ホワイト',
      },
      {
        infomation: 'エンジン：ガソリン',
      },
      {
        infomation: '定員数：5名',
      },
    ],
    car_recommend1: [
      {
        point: '24h貸し出しOK',
      },
      {
        point: 'アメニティ・設備が豊富',
      },
      {
        point: 'クルーズコントロールでエコ運転',
      },
      {
        point: '定員数：5名',
      },
    ],
    car_recommend2: [
      {
      point: 'まだ買ったばかりなので、かなり綺麗な方だと思います。運転席は結構広いのでひざを伸ばしても座ることができますよ。後部座席も乗ってみると意外と広いと思います！'
      }
    ],
    car_recommend3: [
      {
      point: '後ろの席も結構広いのでゴルフバックなら3つほど入るような感じです。'
      }
    ],
    pr1: '24h貸し出し可能',
    pr2: 'クルーズコントロール、カーナビ、TOYOTAセーフティ機能付',
    pr3: 'TOYOTAセーフティ機能付',
    pr4: '定員5人OK',
    tag1: '1ヶ月間貸し出しOK',
    tag2: '駐車場無料使用OK',
    price: '8,700',
    car_type: 'corolla',
    title: 'プリウスの歴史・概要',
    text: 'プリウスの登場は、2001年だ。センタータンクレイアウトを採用し、広大な室内スペースと低燃費性能を実現したモデルとして誕生した。',
  },
  {
    id: 7,
    user_info: [
      {
      name: 'よしぴー',
      pr: '車好きの中でも車を愛している方です！いつも車内を綺麗に掃除するのが日課になってます。笑 ぜひ、僕の愛車で旅行などを楽しんでもらえたら嬉しいです！ご質問あれば連絡くださいね。',
      icon: 'https://img.icons8.com/color/452/batman.png'
      }
    ],
    address: '福岡県福岡市博多区博多駅前',
    main_images: [
      {
        photo: 'https://response.jp/imgs/thumb_h2/1368463.jpg',
      },
      {
        photo: 'https://toyota.jp/pages/contents/prius/004_p_007/4.0/image/top_design_ext.jpg',
      },
      {
        photo: 'https://motor-fan.jp/images/articles/10006723/big_main10006723_20181128205859000000.png',
      },
      {
        photo: 'https://toyota.jp/pages/contents/prius/004_p_007/4.0/image/top_conductor_perf.jpg',
      }
    ],
    car_info: [
      {
        infomation: '満タン時の走行距離：20km',
      },
      {
        infomation: '駆動方式：2WD',
      },
      {
        infomation: '色：ホワイト',
      },
      {
        infomation: 'エンジン：ガソリン',
      },
      {
        infomation: '定員数：5名',
      },
    ],
    car_recommend1: [
      {
        point: '24h貸し出しOK',
      },
      {
        point: 'アメニティ・設備が豊富',
      },
      {
        point: 'クルーズコントロールでエコ運転',
      },
      {
        point: '定員数：5名',
      },
    ],
    car_recommend2: [
      {
      point: 'まだ買ったばかりなので、かなり綺麗な方だと思います。運転席は結構広いのでひざを伸ばしても座ることができますよ。後部座席も乗ってみると意外と広いと思います！'
      }
    ],
    car_recommend3: [
      {
      point: '後ろの席も結構広いのでゴルフバックなら3つほど入るような感じです。'
      }
    ],
    pr1: '24h貸し出し可能',
    pr2: 'クルーズコントロール、カーナビ、TOYOTAセーフティ機能付',
    pr3: 'TOYOTAセーフティ機能付',
    pr4: '定員5人OK',
    tag1: '1ヶ月間貸し出しOK',
    tag2: '駐車場無料使用OK',
    price: '8,700',
    car_type: 'voxy',
    title: 'プリウスの歴史・概要',
    text: 'プリウスの登場は、2001年だ。センタータンクレイアウトを採用し、広大な室内スペースと低燃費性能を実現したモデルとして誕生した。',
  },
]

export default posts;