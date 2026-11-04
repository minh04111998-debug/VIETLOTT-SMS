# Quality Gate Report - srs-campaign-tang-ve-bank.md

> **Ma bao cao:** QGR-20261005-222351-ba  
> **Thoi gian kiem tra:** 2026-10-05 22:23:51  
> **Vai tro thuc thi:** ba  
> **Ket qua tong the:** **[FAIL]**  

---

## 1. Thong Tin Kiem Tra
- **Artifact:** `f:\VIETLOTT-SMS\artifacts\requirements\srs-campaign-tang-ve-bank.md`
- **Quet tu mo ho (Ambiguity):** FAIL
- **Bao mat du lieu (PII):** PASS
- **Tu cam nghiep vu (Banned words):** FAIL

---

## 2. Chi Tiet Ket Qua Quet Tu Dong

### Ambiguity Scanner Output:
```text
≡ƒöì AMBIGUITY SCANNER RUNNING...

ΓÜá∩╕Å  File: f:\VIETLOTT-SMS\artifacts\requirements\srs-campaign-tang-ve-bank.md
   Line 21: Found 'linh hoß║ít'
   > - **Linh hoß║ít trong Cß║Ñu h├¼nh (Admin):** Cho ph├⌐p Quß║ún trß╗ï vi├¬n (Admin) tß╗▒ thiß║┐t lß║¡p, ─æiß╗üu chß╗ënh c├íc ti├¬u ch├¡ chiß║┐n dß╗ïch (k├¬nh bank, trß║íng th├íi TK, ─æiß╗üu kiß╗çn thanh to├ín, ng├ón s├ích, giß╗¢i hß║ín ng├áy) m├á kh├┤ng cß║ºn can thiß╗çp code.
   Line 224: Found 'hiß╗çu quß║ú'
   > - **So that** t├┤i kiß╗âm so├ít chß║╖t chß║╜ hiß╗çu quß║ú khuyß║┐n mß║íi v├á thß╗▒c hiß╗çn ─æß╗æi so├ít t├ái ch├¡nh ─æß╗ïnh kß╗│ vß╗¢i c├íc Ng├ón h├áng ─æß╗æi t├íc.
--------------------------------------------------
Γ¥î Found 2 ambiguous issues across 1 file(s). Please revise to be exact and quantitative.

```

### PII Scanner Output:
```text
≡ƒ¢í∩╕Å PII SCANNER RUNNING...
Γ£à PII SCAN PASS: Kh├┤ng ph├ít hiß╗çn dß╗» liß╗çu nhß║íy cß║úm ch╞░a che.

```

### Banned Words Output:
```text
≡ƒöÄ BANNED WORDS VALIDATOR RUNNING...

ΓÜá∩╕Å  f:\VIETLOTT-SMS\artifacts\requirements\srs-campaign-tang-ve-bank.md:
   Line 21 [linh hoß║ít]: - **Linh hoß║ít trong Cß║Ñu h├¼nh (Admin):** Cho ph├⌐p Quß║ún trß╗ï vi├¬n (Admin) tß╗▒ thiß║┐t lß║¡p, ─æiß╗üu 
   Line 118 [nhiß╗üu]: > Thß╗¥i gian triß╗ân khai chß╗ë c├▓n 2-3 ng├áy l├ám viß╗çc. Luß╗ông tß║╖ng v├⌐ tß╗▒ ─æß╗Öng c├│ nhiß╗üu rß╗ºi ro vß╗ü
   Line 124 [khoß║úng]: | 1 | Ph├ít v├⌐ tß╗▒ ─æß╗Öng | API Core Ticketing bß╗ï Timeout (>30s) hoß║╖c bß║¡n | External Failure |
   Line 224 [hiß╗çu quß║ú]: - **So that** t├┤i kiß╗âm so├ít chß║╖t chß║╜ hiß╗çu quß║ú khuyß║┐n mß║íi v├á thß╗▒c hiß╗çn ─æß╗æi so├ít t├ái ch├¡nh ─æ
   Line 238 [khoß║úng]: - **When** Chß╗ìn khoß║úng thß╗¥i gian tß╗½ `01/08/2026` ─æß║┐n `31/08/2026`, lß╗ìc k├¬nh `VPBank` v├á nh

Γ¥î FAILED: Found 5 instances of banned/ambiguous words.
Please replace with quantitative, concrete specifications.

```

---

## 3. Ket Luan & Buoc Tiep Theo
- [ ] BLOCKING: Can chinh sua cac vi pham tren truoc khi ban giao hoac baseline.
