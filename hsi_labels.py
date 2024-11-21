# Summary of label4Classes:
# -----------------------------------------------
#   Label   -   Label4Class     -   Description
# -----------------------------------------------
#   1**     -       1           -    Healthy
#   2**     -       2           -     Tumor
#   300     -       3           -  Venous blood
#   301     -       3           -       *
#   303     -       3           -       *
#   310     -       3           -       *
#   302     -       4           -  Artery blood
#   320     -       5           -   Dura Matter
#   322     -       5           -       *
#   330     -       6           -      Bone
#   331     -       6           -       *
#  Others   -       7           -    Background
HSI_LABEL_INFO = {
    "0": {
        "Class": "Not-labeled",
        "Type": "Not-labeled",
        "Color": [255, 255, 255],
        "label4Class": 0,
    },
    "100": {
        "Class": "Normal",
        "Type": "NonDefined",
        "Color": [0, 255, 0],
        "label4Class": 1,
    },
    "101": {
        "Class": "Normal",
        "Type": "Grey-Matter",
        "Color": [0, 255, 0],
        "label4Class": 1,
    },
    "102": {
        "Class": "Normal",
        "Type": "White-Matter",
        "Color": [0, 255, 0],
        "label4Class": 1,
    },
    "200": {
        "Class": "Tumour",
        "Pathology": "Primary-GIV",
        "Type": "PureGBM",
        "Color": [255, 0, 0],
        "label4Class": 2,
    },
    "201": {
        "Class": "Tumour",
        "Pathology": "Primary-GIV",
        "Type": "MixedGIV",
        "Color": [255, 0, 0],
        "label4Class": 2,
    },
    "202": {
        "Class": "Tumour",
        "Pathology": "Primary-GIV",
        "Type": "mMGMT",
        "Color": [255, 0, 0],
        "label4Class": 2,
    },
    "203": {
        "Class": "Tumour",
        "Pathology": "Primary-GIV",
        "Type": "1p19q",
        "Color": [255, 0, 0],
        "label4Class": 2,
    },
    "220": {
        "Class": "Tumour",
        "Pathology": "Primary-GIII",
        "Type": "Oligodendroglial",
        "Color": [255, 0, 0],
        "label4Class": 2,
    },
    "221": {
        "Class": "Tumour",
        "Pathology": "Primary-GIII",
        "Type": "Astroglial",
        "Color": [255, 0, 0],
        "label4Class": 2,
    },
    "222": {
        "Class": "Tumour",
        "Pathology": "Primary-GIII",
        "Type": "MixedGIII",
        "Color": [255, 0, 0],
        "label4Class": 2,
    },
    "230": {
        "Class": "Tumour",
        "Pathology": "Primary-GIII",
        "Type": "Ependymoma",
        "Color": [255, 0, 0],
        "label4Class": 2,
    },
    "240": {
        "Class": "Tumour",
        "Pathology": "Primary-GI",
        "Type": "Ganglioglioma",
        "Color": [255, 0, 0],
        "label4Class": 2,
    },
    "241": {
        "Class": "Tumour",
        "Pathology": "Primary-GI",
        "Type": "Meningioma",
        "Color": [255, 0, 0],
        "label4Class": 2,
    },
    "250": {
        "Class": "Tumour",
        "Pathology": "Secondary",
        "Type": "Lung",
        "Color": [255, 0, 0],
        "label4Class": 2,
    },
    "251": {
        "Class": "Tumour",
        "Pathology": "Secondary",
        "Type": "Breast",
        "Color": [255, 0, 0],
        "label4Class": 2,
    },
    "252": {
        "Class": "Tumour",
        "Pathology": "Secondary",
        "Type": "Skin",
        "Color": [255, 0, 0],
        "label4Class": 2,
    },
    "253": {
        "Class": "Tumour",
        "Pathology": "Secondary",
        "Type": "Renal",
        "Color": [255, 0, 0],
        "label4Class": 2,
    },
    "254": {
        "Class": "Tumour",
        "Pathology": "Secondary",
        "Type": "GI",
        "Color": [255, 0, 0],
        "label4Class": 2,
    },
    "255": {
        "Class": "Tumour",
        "Pathology": "Secondary",
        "Type": "Prostate",
        "Color": [255, 0, 0],
        "label4Class": 2,
    },
    "256": {
        "Class": "Tumour",
        "Pathology": "Secondary",
        "Type": "Ovarian",
        "Color": [255, 0, 0],
        "label4Class": 2,
    },
    "257": {
        "Class": "Tumour",
        "Pathology": "Secondary",
        "Type": "Colon",
        "Color": [255, 0, 0],
        "label4Class": 2,
    },
    "270": {
        "Class": "Tumour",
        "Pathology": "Secondary",
        "Type": "Necrosis",
        "Color": [81, 66, 52],
        "label4Class": 2,
    },
    "300": {
        "Class": "Blood",
        "Type": "Generic",
        "Color": [0, 0, 255],
        "label4Class": 3,
    },
    "301": {
        "Class": "Blood",
        "Type": "Venous-Blood-Vessel",
        "Color": [0, 0, 255],
        "label4Class": 3,
    },
    "302": {
        "Class": "Blood",
        "Type": "Arterial-Blood-Vessel",
        "Color": [0, 255, 255],
        "label4Class": 4,
    },
    "303": {
        "Class": "Blood",
        "Type": "NonDefined-Blood-Vessel",
        "Color": [0, 0, 255],
        "label4Class": 3,
    },
    "310": {"Class": "Blood", "Type": "Clot", "Color": [0, 0, 255], "label4Class": 3},
    "320": {
        "Class": "Meninges",
        "Type": "Dura-Mater",
        "Color": [255, 182, 197],
        "label4Class": 5,
    },
    "321": {
        "Class": "Meninges",
        "Type": "Arachnoid",
        "Color": [255, 182, 197],
        "label4Class": 5,
    },
    "322": {
        "Class": "Meninges",
        "Type": "Pia-Mater",
        "Color": [255, 182, 197],
        "label4Class": 5,
    },
    "330": {
        "Class": "External",
        "Type": "Skin",
        "Color": [0, 255, 255],
        "label4Class": 6,
    },
    "331": {
        "Class": "External",
        "Type": "Skull-Bone",
        "Color": [0, 255, 255],
        "label4Class": 6,
    },
    "400": {
        "Class": "Background",
        "Type": "BG-Generic",
        "Color": [0, 0, 0],
        "label4Class": 7,
    },
    "410": {
        "Class": "Background",
        "Type": "Gauze-Without-Blood",
        "Color": [0, 0, 0],
        "label4Class": 7,
    },
    "411": {
        "Class": "Background",
        "Type": "Gauze-With-Blood",
        "Color": [0, 0, 0],
        "label4Class": 7,
    },
    "412": {
        "Class": "Background",
        "Type": "Gauze-Wire",
        "Color": [0, 0, 0],
        "label4Class": 7,
    },
    "420": {
        "Class": "Background",
        "Type": "Surgical-Elements-Metal",
        "Color": [0, 0, 0],
        "label4Class": 7,
    },
    "422": {
        "Class": "Background",
        "Type": "Surgical-Elements-Marker",
        "Color": [0, 0, 0],
        "label4Class": 7,
    },
    "423": {
        "Class": "Background",
        "Type": "Surgical-Elements-Cotton",
        "Color": [0, 0, 0],
        "label4Class": 7,
    },
    "424": {
        "Class": "Background",
        "Type": "Surgical-Elements-Plastic-Pin",
        "Color": [0, 0, 0],
        "label4Class": 7,
    },
    "425": {
        "Class": "Background",
        "Type": "Surgical-Elements-PlasticTrStr",
        "Color": [0, 0, 0],
        "label4Class": 7,
    },
    "426": {
        "Class": "Background",
        "Type": "Surgical-Elements-MetalTrStr",
        "Color": [0, 0, 0],
        "label4Class": 7,
    },
    "427": {
        "Class": "Background",
        "Type": "Surgical-Elements-Green-Cloth",
        "Color": [0, 0, 0],
        "label4Class": 7,
    },
    "440": {
        "Class": "Background",
        "Type": "Specular-Reflection",
        "Color": [0, 0, 0],
        "label4Class": 7,
    },
}
