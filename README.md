contracts에 저희 NFT를 발행할 smart contract들이 들어갑니다.
contract를 metamask에 있는 저희 Goerli ETH에 등록합니다.

scripts/mint-nft.js에서
아래의 37th line이 실제로 NFT를 metamask에 등록한 smart contract를 통해 item을 등록합니다.
mintNFT("https://gateway.pinata.cloud/ipfs/Qmeou5f7ttU98n96mYWfYzKHV7pfRe5rcZBhYznHZCUV7M");

mintNFT의 인자는 이전에 저희가 만든 metadata의 ipfs 링크입니다.


그래서 사용자에게 받은 이미지를 통해 만든 metadata의 ipfs링크를 
scripts/mint-nft.js의 37th line의 mintNFT함수에 인자로
넘겨주어야 합니다.


cmd에서
> node scripts\mint-nft.js
를 입력하면 발행이 이루어집니다.
