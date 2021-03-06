import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

features_to_drop = ['D19_LETZTER_KAUF_BRANCHE',
                    'EINGEFUEGT_AM',
                    'AGER_TYP',
                    'ALTER_KIND1',
                    'ALTER_KIND2',
                    'ALTER_KIND3',
                    'ALTER_KIND4',
                    'D19_BANKEN_ANZ_12',
                    'D19_BANKEN_ANZ_24',
                    'D19_BANKEN_DATUM',
                    'D19_BANKEN_DIREKT',
                    'D19_BANKEN_GROSS',
                    'D19_BANKEN_LOKAL',
                    'D19_BANKEN_OFFLINE_DATUM',
                    'D19_BANKEN_ONLINE_DATUM',
                    'D19_BANKEN_REST',
                    'D19_BEKLEIDUNG_GEH',
                    'D19_BEKLEIDUNG_REST',
                    'D19_BILDUNG',
                    'D19_BIO_OEKO',
                    'D19_DIGIT_SERV',
                    'D19_DROGERIEARTIKEL',
                    'D19_ENERGIE',
                    'D19_FREIZEIT',
                    'D19_GARTEN',
                    'D19_HANDWERK',
                    'D19_HAUS_DEKO',
                    'D19_KINDERARTIKEL',
                    'D19_KOSMETIK',
                    'D19_LEBENSMITTEL',
                    'D19_LOTTO',
                    'D19_NAHRUNGSERGAENZUNG',
                    'D19_RATGEBER',
                    'D19_REISEN',
                    'D19_SAMMELARTIKEL',
                    'D19_SCHUHE',
                    'D19_SOZIALES',
                    'D19_TELKO_ANZ_12',
                    'D19_TELKO_ANZ_24',
                    'D19_TELKO_MOBILE',
                    'D19_TELKO_OFFLINE_DATUM',
                    'D19_TELKO_ONLINE_DATUM',
                    'D19_TELKO_REST',
                    'D19_TIERARTIKEL',
                    'D19_VERSAND_REST',
                    'D19_VERSI_ANZ_12',
                    'D19_VERSI_ANZ_24',
                    'D19_VERSI_OFFLINE_DATUM',
                    'D19_VERSI_ONLINE_DATUM',
                    'D19_WEIN_FEINKOST',
                    'TITEL_KZ']

categorical_features = ['ANREDE_KZ',
                        'CAMEO_DEUG_2015',
                        'CAMEO_DEU_2015',
                        'CJT_GESAMTTYP',
                        'D19_BUCH_CD',
                        'D19_KONSUMTYP',
                        'KK_KUNDENTYP',
                        'D19_SONSTIGE',
                        'D19_TECHNIK',
                        'D19_VERSICHERUNGEN',
                        'D19_VOLLSORTIMENT',
                        'FINANZTYP',
                        'GEBAEUDETYP',
                        'GFK_URLAUBERTYP',
                        'GREEN_AVANTGARDE',
                        'KBA05_MODTEMP',
                        'KBA05_SEG6',
                        'LP_FAMILIE_FEIN',
                        'LP_FAMILIE_GROB',
                        'LP_STATUS_FEIN',
                        'LP_STATUS_GROB',
                        'NATIONALITAET_KZ',
                        'OST_WEST_KZ',
                        'SHOPPER_TYP',
                        'VERS_TYP',
                        'ZABEOTYP',
                        'AKT_DAT_KL',
                        'ALTERSKATEGORIE_FEIN',
                        'CJT_KATALOGNUTZER',
                        'CJT_TYP_1',
                        'CJT_TYP_2',
                        'CJT_TYP_3',
                        'CJT_TYP_4',
                        'CJT_TYP_5',
                        'CJT_TYP_6',
                        'D19_KONSUMTYP_MAX',
                        'DSL_FLAG',
                        'FIRMENDICHTE',
                        'HH_DELTA_FLAG',
                        'KOMBIALTER',
                        'KONSUMZELLE',
                        'MOBI_RASTER',
                        'RT_KEIN_ANREIZ',
                        'RT_SCHNAEPPCHEN',
                        'RT_UEBERGROESSE',
                        'SOHO_KZ',
                        'STRUKTURTYP',
                        'UMFELD_ALT',
                        'UMFELD_JUNG',
                        'UNGLEICHENN_FLAG',
                        'VHA',
                        'VHN',
                        'GEMEINDETYP']

mixed_type_features = ['CAMEO_INTL_2015',
                       'KBA05_BAUMAX',
                       'LP_LEBENSPHASE_FEIN',
                       'LP_LEBENSPHASE_GROB',
                       'PLZ8_BAUMAX',
                       'PRAEGENDE_JUGENDJAHRE',
                       'WOHNLAGE',
                       'KBA13_BAUMAX']

categorical_features += mixed_type_features

ordinal_features = ['ALTERSKATEGORIE_GROB',
                    'BALLRAUM',
                    'D19_BANKEN_ONLINE_QUOTE_12',
                    'D19_GESAMT_ANZ_12',
                    'D19_GESAMT_ANZ_24',
                    'D19_GESAMT_DATUM',
                    'D19_GESAMT_OFFLINE_DATUM',
                    'D19_GESAMT_ONLINE_DATUM',
                    'D19_GESAMT_ONLINE_QUOTE_12',
                    'D19_TELKO_DATUM',
                    'D19_VERSAND_ANZ_12',
                    'D19_VERSAND_ANZ_24',
                    'D19_VERSAND_DATUM',
                    'D19_VERSAND_OFFLINE_DATUM',
                    'D19_VERSAND_ONLINE_DATUM',
                    'D19_VERSAND_ONLINE_QUOTE_12',
                    'EWDICHTE',
                    'FINANZ_ANLEGER',
                    'FINANZ_HAUSBAUER',
                    'FINANZ_MINIMALIST',
                    'FINANZ_SPARER',
                    'FINANZ_UNAUFFAELLIGER',
                    'FINANZ_VORSORGER',
                    'GEBAEUDETYP_RASTER',
                    'HEALTH_TYP',
                    'HH_EINKOMMEN_SCORE',
                    'INNENSTADT',
                    'KBA05_ALTER1',
                    'KBA05_ALTER2',
                    'KBA05_ALTER3',
                    'KBA05_ALTER4',
                    'KBA05_ANHANG',
                    'KBA05_ANTG1',
                    'KBA05_ANTG2',
                    'KBA05_ANTG3',
                    'KBA05_ANTG4',
                    'KBA05_AUTOQUOT',
                    'KBA05_CCM1',
                    'KBA05_CCM2',
                    'KBA05_CCM3',
                    'KBA05_CCM4',
                    'KBA05_DIESEL',
                    'KBA05_FRAU',
                    'KBA05_GBZ',
                    'KBA05_HERST1',
                    'KBA05_HERST2',
                    'KBA05_HERST3',
                    'KBA05_HERST4',
                    'KBA05_HERST5',
                    'KBA05_HERSTTEMP',
                    'KBA05_KRSAQUOT',
                    'KBA05_KRSHERST1',
                    'KBA05_KRSHERST2',
                    'KBA05_KRSHERST3',
                    'KBA05_KRSKLEIN',
                    'KBA05_KRSOBER',
                    'KBA05_KRSVAN',
                    'KBA05_KRSZUL',
                    'KBA05_KW1',
                    'KBA05_KW2',
                    'KBA05_KW3',
                    'KBA05_MAXAH',
                    'KBA05_MAXBJ',
                    'KBA05_MAXHERST',
                    'KBA05_MAXSEG',
                    'KBA05_MAXVORB',
                    'KBA05_MOD1',
                    'KBA05_MOD2',
                    'KBA05_MOD3',
                    'KBA05_MOD4',
                    'KBA05_MOD8',
                    'KBA05_MOTOR',
                    'KBA05_MOTRAD',
                    'KBA05_SEG1',
                    'KBA05_SEG10',
                    'KBA05_SEG2',
                    'KBA05_SEG3',
                    'KBA05_SEG4',
                    'KBA05_SEG5',
                    'KBA05_SEG7',
                    'KBA05_SEG8',
                    'KBA05_SEG9',
                    'KBA05_VORB0',
                    'KBA05_VORB1',
                    'KBA05_VORB2',
                    'KBA05_ZUL1',
                    'KBA05_ZUL2',
                    'KBA05_ZUL3',
                    'KBA05_ZUL4',
                    'KBA13_ALTERHALTER_30',
                    'KBA13_ALTERHALTER_45',
                    'KBA13_ALTERHALTER_60',
                    'KBA13_ALTERHALTER_61',
                    'KBA13_AUDI',
                    'KBA13_AUTOQUOTE',
                    'KBA13_BJ_1999',
                    'KBA13_BJ_2000',
                    'KBA13_BJ_2004',
                    'KBA13_BJ_2006',
                    'KBA13_BJ_2008',
                    'KBA13_BJ_2009',
                    'KBA13_BMW',
                    'KBA13_CCM_1000',
                    'KBA13_CCM_1200',
                    'KBA13_CCM_1400',
                    'KBA13_CCM_0_1400',
                    'KBA13_CCM_1500',
                    'KBA13_CCM_1600',
                    'KBA13_CCM_1800',
                    'KBA13_CCM_2000',
                    'KBA13_CCM_2500',
                    'KBA13_CCM_2501',
                    'KBA13_CCM_3000',
                    'KBA13_CCM_3001',
                    'KBA13_FAB_ASIEN',
                    'KBA13_FAB_SONSTIGE',
                    'KBA13_FIAT',
                    'KBA13_FORD',
                    'KBA13_HALTER_20',
                    'KBA13_HALTER_25',
                    'KBA13_HALTER_30',
                    'KBA13_HALTER_35',
                    'KBA13_HALTER_40',
                    'KBA13_HALTER_45',
                    'KBA13_HALTER_50',
                    'KBA13_HALTER_55',
                    'KBA13_HALTER_60',
                    'KBA13_HALTER_65',
                    'KBA13_HALTER_66',
                    'KBA13_HERST_ASIEN',
                    'KBA13_HERST_AUDI_VW',
                    'KBA13_HERST_BMW_BENZ',
                    'KBA13_HERST_EUROPA',
                    'KBA13_HERST_FORD_OPEL',
                    'KBA13_HERST_SONST',
                    'KBA13_KMH_110',
                    'KBA13_KMH_140',
                    'KBA13_KMH_180',
                    'KBA13_KMH_0_140',
                    'KBA13_KMH_140_210',
                    'KBA13_KMH_211',
                    'KBA13_KMH_250',
                    'KBA13_KMH_251',
                    'KBA13_KRSAQUOT',
                    'KBA13_KRSHERST_AUDI_VW',
                    'KBA13_KRSHERST_BMW_BENZ',
                    'KBA13_KRSHERST_FORD_OPEL',
                    'KBA13_KRSSEG_KLEIN',
                    'KBA13_KRSSEG_OBER',
                    'KBA13_KRSSEG_VAN',
                    'KBA13_KRSZUL_NEU',
                    'KBA13_KW_30',
                    'KBA13_KW_40',
                    'KBA13_KW_50',
                    'KBA13_KW_60',
                    'KBA13_KW_0_60',
                    'KBA13_KW_70',
                    'KBA13_KW_61_120',
                    'KBA13_KW_80',
                    'KBA13_KW_90',
                    'KBA13_KW_110',
                    'KBA13_KW_120',
                    'KBA13_KW_121',
                    'KBA13_MAZDA',
                    'KBA13_MERCEDES',
                    'KBA13_MOTOR',
                    'KBA13_NISSAN',
                    'KBA13_OPEL',
                    'KBA13_PEUGEOT',
                    'KBA13_RENAULT',
                    'KBA13_SEG_GELAENDEWAGEN',
                    'KBA13_SEG_GROSSRAUMVANS',
                    'KBA13_SEG_KLEINST',
                    'KBA13_SEG_KLEINWAGEN',
                    'KBA13_SEG_KOMPAKTKLASSE',
                    'KBA13_SEG_MINIVANS',
                    'KBA13_SEG_MINIWAGEN',
                    'KBA13_SEG_MITTELKLASSE',
                    'KBA13_SEG_OBEREMITTELKLASSE',
                    'KBA13_SEG_OBERKLASSE',
                    'KBA13_SEG_SONSTIGE',
                    'KBA13_SEG_SPORTWAGEN',
                    'KBA13_SEG_UTILITIES',
                    'KBA13_SEG_VAN',
                    'KBA13_SEG_WOHNMOBILE',
                    'KBA13_SITZE_4',
                    'KBA13_SITZE_5',
                    'KBA13_SITZE_6',
                    'KBA13_TOYOTA',
                    'KBA13_VORB_0',
                    'KBA13_VORB_1',
                    'KBA13_VORB_1_2',
                    'KBA13_VORB_2',
                    'KBA13_VORB_3',
                    'KBA13_VW',
                    'KKK',
                    'KONSUMNAEHE',
                    'MOBI_REGIO',
                    'ONLINE_AFFINITAET',
                    'ORTSGR_KLS9',
                    'PLZ8_ANTG1',
                    'PLZ8_ANTG2',
                    'PLZ8_ANTG3',
                    'PLZ8_ANTG4',
                    'PLZ8_GBZ',
                    'PLZ8_HHZ',
                    'REGIOTYP',
                    'RELAT_AB',
                    'RETOURTYP_BK_S',
                    'SEMIO_DOM',
                    'SEMIO_ERL',
                    'SEMIO_FAM',
                    'SEMIO_KAEM',
                    'SEMIO_KRIT',
                    'SEMIO_KULT',
                    'SEMIO_LUST',
                    'SEMIO_MAT',
                    'SEMIO_PFLICHT',
                    'SEMIO_RAT',
                    'SEMIO_REL',
                    'SEMIO_SOZ',
                    'SEMIO_TRADV',
                    'SEMIO_VERT',
                    'WOHNDAUER_2008',
                    'W_KEIT_KIND_HH',
                    'ARBEIT',
                    'D19_TELKO_ONLINE_QUOTE_12',
                    'D19_VERSI_DATUM',
                    'D19_VERSI_ONLINE_QUOTE_12',
                    'KBA13_ANTG1',
                    'KBA13_ANTG2',
                    'KBA13_ANTG3',
                    'KBA13_ANTG4',
                    'KBA13_CCM_1401_2500',
                    'KBA13_GBZ',
                    'KBA13_HHZ',
                    'KBA13_KMH_210',
                    'ALTER_HH']

numeric_features = ['ANZ_HAUSHALTE_AKTIV',
                    'ANZ_HH_TITEL',
                    'ANZ_PERSONEN',
                    'ANZ_TITEL',
                    'GEBURTSJAHR',
                    'KBA13_ANZAHL_PKW',
                    'MIN_GEBAEUDEJAHR',
                    'ANZ_KINDER',
                    'ANZ_STATISTISCHE_HAUSHALTE',
                    'EINGEZOGENAM_HH_JAHR',
                    'EXTSEL992',
                    'VERDICHTUNGSRAUM',
                    'VK_DHT4A',
                    'VK_DISTANZ',
                    'VK_ZG11']

passthrough_features = ['LNR']

class MissingOrUnknownParser(BaseEstimator, TransformerMixin):
    # Class Constructor
    def __init__(self, data_dictionary):
        self._data_dictionary = data_dictionary
    # Return self nothing else to do here
    def fit(self, X, y=None):
        return self

    def _map_nans(self, value, mapping):
        try:
            mapped_value = int(value)
        except:
            mapped_value = value

        try:
            if np.isnan(value):
                mapped_value = -99999
        except:
            pass

        if str(mapped_value) in mapping:
            mapped_value = -99999

        return mapped_value

    # Method that describes what we need this transformer to do
    def transform(self, X, y=None):
        parse_string_list = lambda s: s.strip('[]').split(',')

        for _, row in self._data_dictionary[self._data_dictionary['missing_or_unknown'] != '[]'].iterrows():
            column = row['attribute']
            missing_or_unknown = parse_string_list(row['missing_or_unknown'])
            X[column] = X[column].apply(self._map_nans, args=(missing_or_unknown,))
            X[column] = X[column].replace({-99999: np.nan})

        return X


class RowNaNsDrop(BaseEstimator, TransformerMixin):
    # Class Constructor
    def __init__(self, threshold):
        self._threshold = threshold

    # Return self nothing else to do here
    def fit(self, X, y=None):
        return self

        # Method that describes what we need this transformer to do

    def transform(self, X, y=None):
        row_nans = pd.DataFrame(X.isnull().sum(axis=1) * 100 / X.shape[1], columns=['nan_count'])
        row_nans = row_nans[row_nans['nan_count'] >= self._threshold]

        data_over_treshold = X.iloc[row_nans.index, :]
        X = X.drop(data_over_treshold.index, axis=0)

        return X

class FeatureSelector( BaseEstimator, TransformerMixin ):
  #Class Constructor
  def __init__(self, feature_names, exclude=False):
    self._feature_names = feature_names
    self._exclude = exclude

  #Return self nothing else to do here
  def fit( self, X, y = None ):
    return self

  #Method that describes what we need this transformer to do
  def transform( self, X, y = None ):
    return X.drop(self._feature_names, axis=1) if self._exclude else X[self._feature_names]


class CategoricalTransformer(BaseEstimator, TransformerMixin):
  #Class constructor method that takes in a list of values as its argument
  #def __init__(self)

  #Return self nothing else to do here
  def fit( self, X, y = None  ):
    return self

  def get_feature_names(self):
    return self._feature_names

  #Transformer method we wrote for this transformer
  def transform(self, X , y = None ):
    # Re-encode OST_WEST_KZ
    # X.loc[:, 'OST_WEST_KZ'] = X['OST_WEST_KZ'].map({'W': 1, 'O': 2})

    # Fill missing values with the median value
    X = X.fillna(X.mode().iloc[0])

    # Re-engineer PRAEGENDE_JUGENDJAHRE
    decade = {'1.0': 1, '2.0': 1, '3.0': 2, '4.0': 2, '5.0': 3, '6.0': 3, '7.0': 3, '8.0': 4, '9.0': 4, '10.0': 5,
              '11.0': 5, '12.0': 5, '13.0': 5, '14.0': 6, '15.0': 6}

    movement = {'1.0': 1, '2.0': 2, '3.0': 1, '4.0': 2, '5.0': 1, '6.0': 2, '7.0': 2, '8.0': 1, '9.0': 2, '10.0': 1,
                '11.0': 2, '12.0': 1, '13.0': 2, '14.0': 1, '15.0': 2}


    X['PRAEGENDE_JUGENDJAHRE'] = X['PRAEGENDE_JUGENDJAHRE'].astype('str')
    X['PRAEGENDE_JUGENDJAHRE_DECADE'] = X['PRAEGENDE_JUGENDJAHRE'].replace(decade)
    X['PRAEGENDE_JUGENDJAHRE_MOVEMENT'] = X['PRAEGENDE_JUGENDJAHRE'].replace(movement)
    X = X.drop('PRAEGENDE_JUGENDJAHRE', axis=1)

    # Re-engineer CAMEO_INTL_2015
    X['CAMEO_INTL_2015_WEALTH'] = X['CAMEO_INTL_2015'].apply(lambda x: list(str(x))[0])
    X['CAMEO_INTL_2015_LIFE_STAGE'] = X['CAMEO_INTL_2015'].apply(lambda x: list(str(x))[1])
    X = X.drop('CAMEO_INTL_2015', axis=1)

    cat_numeric = list(set(X.columns.tolist())-set(['OST_WEST_KZ', 'CAMEO_DEU_2015']))
    X[cat_numeric] = X[cat_numeric].astype('int8')

    self._feature_names = X.columns.tolist()

    return X

class PassthroughTransformer(BaseEstimator, TransformerMixin):
  #Class constructor method that takes in a list of values as its argument
  #def __init__(self)

  #Return self nothing else to do here
  def fit( self, X, y = None  ):
    return self

  def get_feature_names(self):
    return self._feature_names

  #Transformer method we wrote for this transformer
  def transform(self, X , y = None ):
    self._feature_names = X.columns.tolist()

    return X