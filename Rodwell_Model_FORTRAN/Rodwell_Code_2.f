      program main

      IMPLICIT DOUBLE PRECISION (A-H,K-M,O-Z)
      character PRNTR*20
      integer i,j,n
      integer jj

      PRNTR = "OUTPUT_MARS.DAT"
      OPEN(unit=10,FILE=PRNTR,STATUS="NEW")

      OPEN(unit=9,FILE="/Users/alanwang/Desktop/input.txt")

      READ(9,*) TZ3 ! hrs
      READ(9,*) MGO ! gallons, initialized bulb volume
      READ(9,*) QBC
      READ(9,*) MF !lbm/hr, Boiler mass flow rate


      READ(9,*) TZ4 !hrs
      READ(9,*) QBC1 ! btu/hr
      READ(9,*) MUG1 ! gal/day, initial withdrawal
      READ(9,*) MF1 ! lbm/hr, boiler mass flow rate
      TZ3E = 88000 ! ten years=88000.0 
      READ(9,*) TZ5 ! hrs
      MUG2 = MUG1 ! gal/day
      READ(9,*) QBC2
      READ(9,*) MF2
      READ(9,*) TZ6
      READ(9,*) QBC3
      READ(9,*) QBC4
      READ(9,*) QBC5

      AL = 0.30 ! Firn loss parameter
      ALPHAI = .0446 ! ft2/hr
      BO = 1.1
      CPA = 0.24  ! Cp air - Changed to Mars value 08/03/18 (was 0.199 ! BTU /lb-F)
      CPI = .5 ! Cp ice
      CPW = 1.0 ! Cp water
      READ(9,*) DEPTH ! ft, initial depth to top of water
      DT = 8.333001E-03 ! hrs (30 secs)
      EIT = 0.0
      E = 0.0
      FI = 0.90
      GAM = 1.0
      H = 10.0
      HA = 1.0  ! Heat transfer between water and air changed Mars value 08/03/18  (original = 0.725)
      HB = 60.0
      HI = 1.0 ! Heat transfer between water and air changed Mars value 08/03/18  (original = 0.725)
      HS = 32.5 ! BTU/hr-ft2-F
      HBN = 24.0
      HSN = 32.5
      HSO = 32.5
      J = 1
      KI = 1.28 !BTU/hr-ft-F, ice/firn conductivity
      MU = 0.0
      MUD = 7549.5  !  1006.61 !  withdrawal rate in gal/min = MUD/(8.04*RHOW) (0 = 0 gal/day)
      MWG =0.0 ! gallons, bulb water volume in gallons
      READ(9,*) MFS ! summer boiler flow rate. lbm/hr
      READ(9,*) MFW ! winter flow rate
      READ(9,*) MUGS ! summer withdrawal, gal/day
      READ(9,*) MUGW ! winter withdrawal, gal/day

      MGW = 1106533.0 !
      N = 1
      OMEGA = 5.399
      PI = 3.141593
      PL = 0.0
      PM = 0.0
      PLT = 0.0
      PMT = 0.0
      PRWT = 0.0


      QS = 0.0
      QT = 0.0
      QTT = 0.0
      QIT = 0.0
      RA = 1.5 !ft, drill radius
      RHOIS = 45.0 !lbm/ft3, start close-off density of firn
      RHOIM = 57.54 !lbm/ft3, max firn density
      RHOW = 62.6 ! lbm/ft3, water density
      RO = RA ! ft

      TAUP = 0.0
      TI = 0.0
      TIS = 0.0
      TP = 8.0 ! 24.0
      TPI = 8.0 ! 24.0
      TPIW = 8.0 ! 24.0
      TZ1 = 8760 ! 8760 days is one year
      TZ2 = 240.0 ! 24.0
      TZS = TZ1 - TZ6 ! Summer duration (days)

      TF = 32.0
      READ(9,*) TICE ! F, Firn Temperature
      READ(9,*) TWB ! F, Boiler water temperture
      TA = TICE
      TS = TICE
      TW = TWB
! depth at which shut-off starts in firn.

        ZS = ((RHOIS - 20.18)/2.4996)**(1/0.45) ! Greenland data
! ZS = (.144-SQRT((.144)**2-4.0*(RHOIS-21.79)*.00017894))/(2.0*.00017894)  ! Antarctic data
      ! ZS=H

      D = 2.82843*RO !ft, diameter of bulb
      MFA = MF
      MW = PI * RA * RA * H * RHOW !lbm, water mass
      MWO = MW
      HWB = DEPTH + H !ft, depth to well bottom
      MWGA = MW / (.134 * RHOW) ! gallons, convert bulb water mass to volume in gallons
      LE = 144.0 + CPI * (TF - TICE) * OMEGA
      AB = PI * D**2./4.0 ! ft2, air-water interface area
      HW = H ! ft, water depth
      AS = 2.0*PI*D*H/3.0 ! ft2, water-ice contact area
      VW = PI*D**2.*H/8.0 ! ft3, water volume in bulb
      AI = 2.0 * PI * RA * DEPTH ! ft2, air-ice contact area
      VA = PI * RA * RA * DEPTH ! ft3, air volume

130       WRITE(10,3000)
3000       format(1x,'Withdrawal Rate = 100 gal/day')
140       WRITE(10,3001) TWB
3001       format(1x,' BOILER WATER TEMP DEG F = ',F9.2)
150       WRITE(10,3002) MF
3002       format(1x,' BOILER WATER FLOW RATE lbm/hr = ',F9.2)
160       WRITE(10,3003) HS
3003       format(1x,' CONVECTIVE COEFFICIENT BTU/HR-FT2-F = ',F9.2)
      WRITE(10,3013) RA
3013       format(1x,' INITIAL DRILL RADIUS FT = ',F9.2)
      WRITE(10,3014) DEPTH
3014       format(1x,' DEPTH TO TOP OF WATER AT START FT = ',F9.2)
180       WRITE(10,3005) D
3005       format(1x,' INITIAL PARABOLIC WATER DIAMETER D FT = ',F9.2)
191       WRITE(10,3007) HW
3007       format(1x,' INITIAL PARABOLIC WATER HEIGHT HW FT = ',F9.2)
200       WRITE(10,3008) TW
3008       format(1x,'INITIAL WATER TEMP TW DEG F = ',F9.2)
201       WRITE(10,3009) TA
3009       format(1x,' INITIAL AIR TEMP TA DEG F = ',F9.2)
202       WRITE(10,3010) TS
3010       format(1x,' INITIAL ICE SURFACE TEMP TS DEG F = ',F9.2)
210       WRITE(10,3011) TICE
3011       format(1x,'AMBIENT ICE TEMP DEG F = ',F9.2)
220       WRITE(10,3012) LE
3012       format(1x,'EFFECTIVE LATENT HEAT BTU/LB = ',F9.2)
221       WRITE(10,*) 'TIME IN HRS, WATER VOL MW GALLONS, ICE AREA AI FT2,& AIR VOL VA FT3'
222       WRITE(10,*)
252       WRITE(10,*) '     TIME   TW      TA    TS       MW     D    HW    HWB        AI         VA'
253       WRITE(10,2001) TI, TW, TA, TS, MWGA, D, HW, HWB, AI, VA
3030       format(1x,F8.2, 3F7.2,F9.2,2F6.2,F7.2,F7.2)
260       DO I=1,112500000
            IF (MWG .GT. MGO) GOTO 1220 ! bulb water volume .gt. initilaize volume
            IF (TI .GT. TZ3) GOTO 1220 ! time .gt. formation period
            IF (J .EQ. 1) GOTO 280 ! not sure why we branch here, bulb formation?
 400            IF (TI .LT. TAUP) then ! not sure what taup is
                  MF = 0.0
                  MUG = MUGA
                  MU = MUD
            else
                  MF = MFA
                  MUG = 0.0
                  MU = 0.0
            end if
! determine firn density
280             ZP = HWB-H/2.0 ! ft, average bulb depth

! This is for Greenland data at Summit
      RHOI = 20.18 + 2.4996 * ZP**0.45 ! shallow: ZP .le. 394 ft
      IF(ZP .GT. 394) then
      RHOI = RHOIM
      end if

! This is for Antarctic data - test
!
!            if(ZP .GT. 520) then
!                  RHOI=RHOIM
!            ELSEIF (ZP .GT.320) then
!                  RHOI = .04*ZP + 36.74
!            ELSE
!                  RHOI=21.79+0.144*ZP-0.00017894*ZP**2
!            END IF

! compute the change in water depth, h (eq. 7)
291             DELH = 16.0*H*(HS*(TW-TF)-QS)*DT/(RHOI*LE*3.0*(2.0*GAM*H+D))
            HP = H+DELH
            DP = D+GAM*DELH
            HWBP = HWB+DELH
! assumes full shut-off of water leakage into firn at ZS.
            ZPS = HWB-ZS
            ASP = 2.0*PI*D*H/3.0 ! all of surface area in fully porous firn
            IF(ZPS .GT. H) then ! bulb below firn shut-off
                  ASP = 0.0 ! none of bulb surface area in fully porous firn
            else IF(HWB .GT. ZS) then ! well bottom is deeper than firn shut-off
                  ZPP = (ZS+HWB-H)/2.0 ! average depth of portion of bulb inporous firn
                  ASP = 2.0*PI*D*H*(1.0-(ZPS/H)**1.5)/3.0 ! portion of bulb in porous firn
! GREENLAND
            RHOI = 20.18 + 2.4996 * ZPP**0.45 ! firn density
! ANTARCTICA
! RHOI=21.79+0.144*ZP-0.00017894*ZP**2
            endif
283             MUL = AL*ASP*(RHOIS - RHOI) ! water mass lost to firn
            IF(MF .EQ. 0.0) GOTO 284
            TWB = QBC/(CPW*MF) + TW
284             TWP = TW+(MF*(TWB-TW)-HS*AS*(TW-TF)*(1.0/CPW+(TW-TF)/LE-QS/(LE*HS))-            HA*AB*(TW-TA)/CPW)*DT/MW
            MWP = MW+(((TW-TF)*HS-QS)*AS/LE-MU-MUL)*DT
            MWG = MWP / (.134 * RHOW)
            VWP = MWP / RHOW
            HF = SQRT(8.0*VWP*HP/PI)/DP
            DF = DP*SQRT(HF/HP)
            HW = HF
            EP = CPW * (TWB - TWP) * MF * DT
            E = E + EP
            PMP = MU*DT
            PM = PM + PMP
            PLP = MUL*DT
            PL = PL + PLP
            AIP = AI+PI*(DP**2-D**2)/4.0 + PI*DP*(HP-HF)
            VAP = VA + PI*(DP**2*HP-DF**2*HF)/8.0
            H = HF
            D = DF
            TI = DT + TI
            Q = HI * (TA - TS)
            QI = Q * DT * AI
            QT = QT + Q * DT
            QIT = QIT + QI
            QB = QT / TI
            TAU = ALPHAI * TI / (RO ** 2)
            RHOA = 6 / (TA + 460.0) ! Mars value for CO2 atmosphere = 0.4758 [from 39.685]
            TAP = TA+(HA*AB*(TW-TA)+HI*AI*(TS-TA))*DT/(RHOA*VA*CPA)
418             FB = 5.0*BO**3.0/36.0-BO/4.0+1.0/9.0+(1.0/3.0-BO/2.0)*LOG(BO) - TAU*(BO-1.0+LOG(BO))
            FBP = 5.0*(BO**2)/12.0 - .25-LOG(BO)/2.0+(1.0/3.0-BO/2.0)/BO- TAU*(1.0+1.0/BO)
            BP = BO - FB /FBP
            BZ = ABS(BP - BO)
            IF(BZ .lt. .0001) GOTO 425
            BO = BP
            GOTO 418
425             B = BP
            BO = BP +.1
            TS = TICE+QB*RO*(B-1.0)*LOG(B)/(KI*(B-1.0+LOG(B)))
            IF(J .EQ. 1) GOTO 1031
            IF(TI .gt.TPW) GOTO 1130
1028             IF(TI .gt. TP) GOTO 1131
            GOTO 560
1031             IF(TI .gt. TP) GOTO 1128
560             CONTINUE
            HWB = HWBP
            TW = TWP
            TA = TAP
            MW = MWP
            AS = 2.0*PI*D*H/3.0
            AB = PI*D**2/4.0
            AI = AIP
            VA = VAP
            IF (D .GT. 60.0) GOTO 1010
            HS = HSO
            GOTO 1040
1010             HS = HSN
1040             IF(TW .LT. 32.0001) GOTO 1075
1041             IF(TI .GT. TZ2) GOTO 1220
            IF(TI .GT. TZ1) GOTO 1220
1070       end do
      GOTO 1760
1075       TW = 32.0
      GOTO 1041
1128       WRITE(10,2001) TI, TWP, TAP, TS, MWG, D, HW, HWBP, AIP, VAP
      TP = TP + TPI
      TPW = TP
      GOTO 560
1130       WRITE(10,2001) TI, TWP, TAP, TS, MWG, D, HW, HWBP, AIP, VAP
2001       format(1x, F8.1, 3F7.2, F9.1, 2F6.2, F7.2, 2F11.2)
      ! WRITE(10,777) QWA
!777      format(1x,' Water Pool Surface to Air in Cavity = ',F9.2)
      TPW = TPW + TPIW
      GOTO 1028
1131       TP = TP + TPI
      TAUP = TP+MUGA*.134*RHOW/MUD-TPI
      GOTO 560
1220       WRITE(10,2001) TI, TWP, TAP, TS, MWG, D, HW, HWBP, AIP, VAP
2000       format(1X,6F9.2)
1280       WRITE(10,*)
      EI = E - EIT
      ESR = EI/(TI-TIS)
      EIT = E
      PRW = MW-MWO + PM
      PRWT = PRWT+PRW
      PLT = PLT+PL
      PMT = PMT+PM
      EKT = PRWT*19500.0/E
      EK = PRW * 19500.0 / EI
      PMG = PM/(.134*RHOW)
      PM = 0.0
      PLG = PL/(.134*RHOW)
      PL = 0.0
      MWO = MW
      EF = E / 140000.0
      EFI = EI / 140000.0
      QITI = QIT - QTT
      QTT = QIT
1340       WRITE(10,3040) E
3040       format(1x, ' TOTAL ENERGY INPUT BTU = ',E15.6)
      WRITE(10,3041) EI
3041       format(1x, ' SEASONAL ENERGY INPUT BTU = ',E15.6)
      WRITE(10,3051) EFI
3051       format(1x, ' SEASONAL ENERGY INPUT GAL FUEL = ',F15.2)
      WRITE(10,3042) ESR
3042       format(1x, ' SEASONAL ENERGY RATE BTU/HR = ',F15.2)
1370       WRITE(10,3050) EF
3050       format(1x, ' TOTAL ENERGY INPUT GAL FUEL = ',F15.2)
      WRITE(10,3063) EKT
3063       format(1x, ' AVERAGE LB. WATER PER LB. FUEL = ',F15.2)
1400       WRITE(10,3060) EK
3060       format(1x, ' SEASONAL LB. WATER PER LB. FUEL = ',F15.2)
1401       WRITE(10,3070) QIT
3070       format(1x, ' ENERGY FROM AIR TO ICE BTU = ',E15.6)
      WRITE(10,3071) QITI
3071       format(1x, ' SEASONAL ENERGY LOSS, AIR TO ICE BTU = ',E15.6)
      WRITE(10,3064) PMT/(.134*RHOW)
3064       format(1x, ' TOTAL WATER WITHDRAWN GAL = ',F15.2)
      WRITE(10,3061) PMG
3061       format(1x, ' SEASONAL WATER WITHDRAWN GAL = ',F15.2)
      WRITE(10,3065) PLT/(.134*RHOW)
3065       format(1x, ' TOTAL WATER LOSS GAL = ',F15.2)
      WRITE(10,3062) PLG
3062       format(1x, ' SEASONAL WATER LOSS GAL = ',F15.2)
1430       WRITE(10,*)
      IF(N .EQ. 1) GOTO 1490
      IF(N .EQ. 2) GOTO 1204
      IF(N .EQ. 3) GOTO 1540

      IF(N .EQ. 4) GOTO 1520
      IF(N .EQ. 5) GOTO 1500

!      IF(N .EQ. 6) GOTO 1520
!      IF(N .EQ. 7) GOTO 1500

!      IF(N .EQ. 8) GOTO 1520
!      IF(N .EQ. 9) GOTO 1500

!      IF(N .EQ. 10) GOTO 1520
!      IF(N .EQ. 11) GOTO 1500

!      IF(N .EQ. 12) GOTO 1520
!      IF(N .EQ. 13) GOTO 1500

!      IF(N .EQ. 14) GOTO 1520
!      IF(N .EQ. 15) GOTO 1500

!      IF(N .EQ. 16) GOTO 1520
!      IF(N .EQ. 17) GOTO 1500

!      IF(N .EQ. 18) GOTO 1520
!      IF(N .EQ. 19) GOTO 1500

!      IF(N .EQ. 20) GOTO 1520
!      IF(N .EQ. 21) GOTO 1500

      IF(N .EQ. 22) GOTO 1760
1490       MGO = MGW
      MF = MF1
      MUGA = MUG1
      N = N + 1
      J = J + 1
      JJ = 1 ! year
      MFA = MF
      TIS = TI
      ! TP = INT(TI/24.0)*24.0+TPI
      TP = INT(TI/1.0)*1.0+TPI
      TZ1 = TP+TZ4
      TZ2 = TZ1+TZ5
      TZ3 = TZ3E
      QBC = QBC1
      GOTO 1210
1500       CONTINUE
      MGO = MGW
      MUGA = MUGW
      MFA = MFS
      N = N+1
      MU = MUD
! Greenland
      TZ2 = TZ1+TZS
! Antarctica
! TZ2=TZ1+2976.0
      TIS = TI
      QBC = QBC5
      GOTO 1553
1520       CONTINUE
      MGO = MGW
      MUGA = MUGS
      MFA = MFS
      N = N+1
      MU = MUD
      JJ = JJ+1
      TIS = TI
! Greenland
      TZ1 = TZ2+TZ6
! Antarctica
! TZ1=TZ2+5784.0
      QBC = QBC4
      GOTO 1551
1540       CONTINUE
      MGO = MGW
      MUGA = MUGW
      MFA = MFS
      N = N+1
      JJ = 1
      MU = MUD
      TIS = TI
      QBC = QBC3
! Greenland
      TZ2 = TZ1+TZS
! Antarctica
! TZ2=TZ1+2976.0
      GOTO 1550
1204       CONTINUE
      MGO = MGW
      MF = MF2
      MUGA = MUG2
      N = N+1
      JJ = 1
      MFA = MF
      MU = MUD
      TIS = TI
      TZ1 = TZ2+TZ6
      QBC = QBC2
      GOTO 1550
1210       CONTINUE
      MU = MUD
      TAUP = TP+MUGA*.134*RHOW/MUD-TPI
      TPIW = 168.0
1550       WRITE(10,8000) JJ
8000       format(1x,' YEAR ',I3)
      WRITE(10,6000)
6000       format(1x,' STANDBY or Water Withdrawal')
      GOTO 1555
1551       WRITE(10,8000) JJ
      WRITE(10,6001)
6001       format(1x,'Summer Water Withdrawal')
      GOTO 1555
1553       WRITE(10,8000) JJ
      WRITE(10,6002)
6002       format(1x,' Winter Water Withdrawal')
1555       WRITE(10,*)
1580       WRITE(10,4010) MFA

4010       format(1x,'BOILER WATER FLOW RATE lbm/hr = ',F9.2)
      WRITE(10,4011) TWB
4011       format(1x,'BOILER WATER TEMPERATURE DEG F = ',F9.2)
1610       WRITE(10,4020) MUGA
4020       format(1x,'WATER WITHDRAWAL GAL/DAY = ',F9.2)
      WRITE(10,4021) MUD/(8.04*RHOW)
4021       format(1x,'WITHDRAWAL FLOW RATE GAL/MIN = ',F9.2)
1640       WRITE(10,4030) HS
4030       format(1x,'CONVECTIVE COEFF AFTER R=30 FT BTU/HR-FT2-F = ',F9.2)
1672       WRITE(10,5050) TI
5050       FORMAT(1X,'START WITHDRAWAL AT HOUR =' , F9.2)
      WRITE(10,*)
      GOTO 400
1760       WRITE(10,*)
1790       WRITE(10,4050) E
4050       format(1x,' TOTAL ENERGY INPUT BTU            = ', E15.6)
1820       WRITE(10,4060) E / 140000
4060       format(1x,' TOTAL ENERGY INPUT GAL FUEL            = ', E15.2)
1821       WRITE(10,4070) QIT
4070       format(1x,' TOTAL ENERGY LOSS AIR TO ICE BTU            = ', E15.6)
1850       END
