# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 11:11:15 2017

@author: paul
"""

from supsisim.block import Block


libs = dict()
libs['can'] = [ \
    Block(name='Baumer_enc', outp=1, icon='ENC', params='baumer_EncBlk|Device ID: 0x01|Resolution: 500'),
    Block(name='Epos_AD', outp=1, icon='AD', params='epos_areadBlk|Device ID: 0x01|Channel [0/1]: 0'),
    Block(name='Epos_enc', outp=1, icon='ENC', params='epos_EncBlk|Device ID: 0x01|Resolution: 1000'),
    Block(name='Epos_mot_I', inp=1, icon='MOT_I', params='epos_MotIBlk|Device ID: 0x01|Prop. gain: 2200|Integ. gain: 500'),
    Block(name='Epos_mot_X', inp=1, icon='MOT_X', params='epos_MotXBlk|Device ID: 0x01|Prop. gain: 126|Integ. gain: 325|Deriv. gain: 238|Vel. FeedForw: 0|Acc. Feed Forw.:1'),
    Block(name='Maxon_enc', outp=1, icon='ENC', params='maxon_EncBlk|Device ID: 0x01|Resolution: 1000'),
    Block(name='Maxon_mot_I', inp=1, icon='MOT_I', params='maxon_MotBlk|Device ID: 0x01|Prop. gain: 2200|Integ. gain: 500'),
    Block(name='Mclm_AD', outp=1, icon='AD', params='MCLM_ADBlk|Device ID: 0x01'),
    Block(name='Mclm_enc', outp=1, icon='ENC', params='MCLM_EncBlk|Device ID: 0x01|Resolution: 125000'),
    Block(name='Mclm_mot_X', inp=1, icon='MOT_X', params='MCLM_MotXBlk|Device ID: 0x01|Resolution: 125000'),
    Block(name='Mclm_CO_enc', outp=1, icon='ENC', params='MCLM_CO_EncBlk|Device ID: 0x01|Resolution: 125000'),
    Block(name='Mclm_CO_mot_X', inp=1, icon='MOT_X', params='MCLM_CO_MotXBlk|Device ID: 0x01|Resolution: 125000') ]

libs['comedi'] = [ \
    Block(name='AD', outp=1, icon='AD', params="comediADBlk|Device: '/dev/comedi0'|Channel: 0|Range: 0"),
    Block(name='DA', inp=1, icon='DA', params="comediDABlk|Device: '/dev/comedi0'|Channel: 0|Range: 0"),
    Block(name='DI', outp=1, icon='DI', params="comediDIBlk|Device: '/dev/comedi0'|Channel: 0"),
    Block(name='DO', inp=1, icon='DO', params="comediDOBlk|Device: '/dev/comedi0'|Channel: 0|Threshold: 1.0") ]

libs['common'] = [ \
    Block(name='Const', outp=1, icon='CONST', params='constBlk|Value: 0'),
    Block(name='PulseGenerator', outp=1, icon='SQUARE', params='squareBlk|Amplitude: 1|Period: 4|Width: 2|Bias: 0|Delay: 0'),
    Block(name='Step', outp=1, icon='STEP', params='stepBlk|Step Time: 1|Step Value: 1'),
    Block(name='LTI_continous', inp=1, outp=1, iosetble=True, icon='CSS', params='cssBlk|System: sys|Initial conditions: 0'),
    Block(name='LTI_discrete', inp=1, outp=1, iosetble=True, icon='DSS', params='dssBlk|System: sys|Initial conditions: 0'),
    Block(name='Gain', inp=1, outp=1, iosetble=True, icon='MULT', params='matmultBlk|Gains: 1'),
    Block(name='Sub', inp=2, outp=1, icon='PM', params='sumBlk|Gains: [1,-1]'),
    Block(name='Sum', inp=2, outp=1, iosetble=True, icon='SUM', params='sumBlk|Gains: [1,-1]'),
    Block(name='Print', inp=1, iosetble=True, icon='PRINT', params='printBlk'),
    Block(name='Saturation', inp=1, outp=1, icon='SATUR', params='saturBlk|Upper saturation:10|Lower saturation: -10') ]

libs['input'] = [ \
    Block(name='Const', outp=1, icon='CONST', params='constBlk|Value: 0'),
    Block(name='Extdata', outp=1, icon='EXTDATA', params='extdataBlk|Data length: 1000|File name: data'),
    Block(name='Sine_wave', outp=1, icon='SINUS', params='sineBlk|Amplitude: 1|Freq: 1|Phase: 0|Bias: 0|Delay: 0'),
    Block(name='PulseGenerator', outp=1, icon='SQUARE', params='squareBlk|Amplitude: 1|Period: 4|Width: 2|Bias: 0|Delay: 0'),
    Block(name='Step', outp=1, icon='STEP', params='stepBlk|Step Time: 1|Step Value: 1') ]
                      
libs['linear'] = [ \
    Block(name='LTI_continous', inp=1, outp=1, iosetble=True, icon='CSS', params='cssBlk|System: sys|Initial conditions: 0'),
    Block(name='LTI_discrete', inp=1, outp=1, iosetble=True, icon='DSS', params='dssBlk|System: sys|Initial conditions: 0'),
    Block(name='Init_enc', inp=1, outp=1, icon='INIT', params='init_encBlk|Trigger Time: 1|Default Output: 0|Offset: 0'),
    Block(name='Integral', inp=1, outp=1, icon='INTG', params='intgBlk|Initial conditions: 0'),
    Block(name='Gain', inp=1, outp=1, iosetble=True, icon='MULT', params='matmultBlk|Gains: 1'),
    Block(name='Delay', inp=1, outp=1, icon='DELAY', params='zdelayBlk|Initial conditions: 0')]

libs['math'] = [ \
    Block(name='Sub', inp=2, outp=1, icon='PM', params='sumBlk|Gains: [1,-1]'),
    Block(name='Sum', inp=2, outp=1, iosetble=True, icon='SUM', params='sumBlk|Gains: [1,-1]'),
    Block(name='Prod', inp=2, outp=1, iosetble=True, icon='PROD', params='prodBlk') ]

libs['nonlin'] = [ \
    Block(name='Abs', inp=1, outp=1, icon='ABS', params='absBlk'),
    Block(name='FMU', inp=1, outp=1, iosetble=True, icon='FMU', params="FmuBlk|IN_REF: ['u']|OUT_REF: ['y']|FMU_NAME: ''|Major step: 0.01|Feedthrough: 0"),
    Block(name='Lookup', inp=1, outp=1, icon='LOOKUP', params='lutBlk|Coeff : [1,0]'),
    Block(name='Saturation', inp=1, outp=1, icon='SATUR', params='saturBlk|Upper saturation:10|Lower saturation: -10'),
    Block(name='Switch', inp=3, outp=1, icon='SWITCH', params='switchBlk|Condition [0 < or 1 >] : 0|Compare Value: 0.5|Persistence [0 no or 1 yes]: 0'),
    Block(name='Trig', inp=1, outp=1, icon='TRIG', params='trigBlk|sin->1 cos->2 tan->3: 1'),
    Block(name='Generic_C_Block', inp=1, outp=1, iosetble=True, icon='CBLOCK', params="genericBlk|States: [0,0]|FeedForw: 0|Real pars: []| Int pars:[]|String: ''| Function name: 'test'") ]

libs['output'] = [ \
     Block(name='Plot', inp=1, iosetble=True, icon='PRINT', params='printBlk') ]

libs['Socket'] = [ \
    Block(name='socket', inp=1, iosetble=True, icon='SOCK', params="unixsocketCBlk|Socket: 'bsock'"),
    Block(name='Socket', outp=1, iosetble=True, icon='SOCK', params="unixsocketSBlk|Socket: 'ssock'|Default outputs:[0.]") ]
        
libs['testlib'] = [ \
    Block(name='test1', inp=[('a', -40, -20), ('b', -40, 20)], outp=[('z', 40, 0)], iosetble=True, icon='test1', params='sumBlk|Gains: [1,-1]'), 
    Block(name='multiot_dpll_dig', 
          inp= [('i_clk', -150, -220), 
                ('clk_HS_DBB', -150, -180), 
                ('i_rst_an', -150, -140), 
                ('i_ch_sw', -150, -100), 
                ('i_modulation_enable', -150, -60), 
                ('i_modulation_PM_data', -150, -20), 
                ('i_modulation_FM_data', -150, 20), 
                ('i_tdc', -150, 60), 
                ('i_cnt_fb', -150, 100), 
                ('i_cnt_ref', -150, 140), 
                ('w_rst_n', -150, 180), 
                ('w_fcw', -150, 220)], 
          outp=[('o_dco_pvt', 150, -220), 
                ('o_dco_acq', 150, -180), 
                ('o_dco_trk', 150, -140), 
                ('o_dco_mod', 150, -100), 
                ('o_n', 150, -60), 
                ('o_dtc_ref_row', 150, -20), 
                ('o_dtc_ref_col', 150, 20), 
                ('o_dtc_fb_row', 150, 60), 
                ('o_dtc_fb_col', 150, 100)], 
          iosetble=True, 
          icon='multiot_dpll_dig', 
          params=''), 
    Block(name='dco', 
          inp= [('i_pvt', -150, -60), 
                ('i_acq', -150, -20), 
                ('i_trk', -150, 20), 
                ('i_mod', -150, 60)], 
          outp=[('o_lop', 150, -60), 
                ('o_lon', 150, -20)], 
          iosetble=True, 
          icon='dco', 
          params=''), 
    Block(name='dtc', 
          inp= [('i_clk_in', -150, -60), 
                ('i_dtc_row', -150, -20), 
                ('i_dtc_col', -150, 20), 
                ('i_phase_sel', -150, 60)], 
          outp=[('o_clk_out', 150, -60), 
                ('o_phase_sel', 150, -20)], 
          iosetble=True, 
          icon='dtc', 
          params=''), 
    Block(name='div28', 
          inp= [('i_cp', -150, -120), 
                ('i_cn', -150, -80), 
                ('i_ena_lo', -150, -40)], 
          outp=[('o_div2', 150, -120), 
                ('o_div8', 150, -80), 
                ('o_div16', 150, -40), 
                ('o_p000', 150, 0), 
                ('o_p090', 150, 40), 
                ('o_p180', 150, 80), 
                ('o_p270', 150, 120)], 
          iosetble=True, 
          icon='div28', 
          params=''), 
    Block(name='divn', 
          inp= [('i_clk_in', -150, -40), 
                ('i_rst_an', -150, 0), 
                ('i_div', -150, 40)], 
          outp=[('o_clk_out', 150, -40)], 
          iosetble=True, 
          icon='divn', 
          params=''), 
    Block(name='dtc_delay', 
          inp= [('i_a', -150, -60), 
                ('i_row', -150, -20), 
                ('i_col', -150, 20), 
                ('i_res_tune', -150, 60)], 
          outp=[('o_zn', 150, -60)], 
          iosetble=True, 
          icon='dtc_delay', 
          params=''), 
    Block(name='pfd', 
          inp= [('i_ref', -150, -60), 
                ('i_fb', -150, -20), 
                ('i_rstref_n', -150, 20), 
                ('i_rstfb_n', -150, 60)], 
          outp=[('o_upn', 150, -60), 
                ('o_dnn', 150, -20)], 
          iosetble=True, 
          icon='pfd', 
          params=''), 
    Block(name='tdc', 
          inp= [('i_ref', -150, -100), 
                ('i_refd_n', -150, -60), 
                ('i_fb', -150, -20), 
                ('i_fbd_n', -150, 20), 
                ('i_cap_ref', -150, 60), 
                ('i_cap_fb', -150, 100)], 
          outp=[('o_tdc', 150, -100), 
                ('o_sample_fb', 150, -60), 
                ('o_cnt_fb', 150, -20), 
                ('o_ckdig', 150, 20), 
                ('o_rstpfd_n', 150, 60), 
                ('o_rstcap', 150, 100)], 
          iosetble=True, 
          icon='tdc', 
          params=''), 
    Block(name='dpa_preproc', 
          inp= [('i_clk_lo', -150, -200), 
                ('i_clk_hi', -150, -160), 
                ('i_rst_an', -150, -120), 
                ('i_en', -150, -80), 
                ('i_ble_en', -150, -40), 
                ('i_dia', -150, 0), 
                ('i_di', -150, 40), 
                ('i_del_en', -150, 80), 
                ('i_bypass_en', -150, 120), 
                ('i_bypass_base', -150, 160), 
                ('i_bypass_delta', -150, 200)], 
          outp=[('o_pa_base_hi_th', 150, -200), 
                ('o_pa_base_lo_bin', 150, -160), 
                ('o_pa_delta_0', 150, -120), 
                ('o_pa_delta_1', 150, -80), 
                ('o_pa_delta_2', 150, -40), 
                ('o_pa_delta_3', 150, 0)], 
          iosetble=True, 
          icon='dpa_preproc', 
          params=''), 
    Block(name='dpa_preproc_6bPA', 
          inp= [('w_LOP_RF', -150, -180), 
                ('w_LON_RF', -150, -140), 
                ('w_LOP_HS_DBB', -150, -100), 
                ('w_LOP_AM', -150, -60), 
                ('w_LON_AM', -150, -20), 
                ('i_modulation_enable', -150, 20), 
                ('i_modulation_AM_data', -150, 60), 
                ('i_rst_an', -150, 100), 
                ('i_rst_n', -150, 140), 
                ('i_del_en', -150, 180)], 
          outp=[('o_pa_base_hi_th', 150, -180), 
                ('o_pa_base_lo_bin', 150, -140)], 
          iosetble=True, 
          icon='dpa_preproc_6bPA', 
          params=''), 
    Block(name='dpa_preproc_ble', 
          inp= [('w_LOP_RF', -150, -120), 
                ('w_LON_RF', -150, -80), 
                ('w_LOP_AM', -150, -40), 
                ('i_modulation_enable', -150, 0), 
                ('i_modulation_AM_data', -150, 40), 
                ('i_rst_an', -150, 80), 
                ('i_rst_n', -150, 120)], 
          outp=[('w_am_data', 150, -120)], 
          iosetble=True, 
          icon='dpa_preproc_ble', 
          params=''), 
    Block(name='lo_divider', 
          inp= [('i_LOP', -150, -140), 
                ('i_LON', -150, -100)], 
          outp=[('o_LOP_PD', 150, -140), 
                ('o_LON_PD', 150, -100), 
                ('o_LOP_RF', 150, -60), 
                ('o_LON_RF', 150, -20), 
                ('o_LOP_AM', 150, 20), 
                ('o_LON_AM', 150, 60), 
                ('o_LON_HS_DBB', 150, 100), 
                ('o_LOP_HS_DBB', 150, 140)], 
          iosetble=True, 
          icon='lo_divider', 
          params='')]

default = 'common'
