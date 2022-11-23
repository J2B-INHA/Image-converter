contracts에 저희 NFT를 발행할 smart contract들이 들어갑니다.
contract를 metamask에 있는 저희 Goerli ETH에 등록합니다.

scripts/mint-nft.js에서
아래의 37th line이 실제로 NFT를 metamask에 등록한 smart contract를 통해 item을 등록합니다.
mintNFT("https://gateway.pinata.cloud/ipfs/Qmeou5f7ttU98n96mYWfYzKHV7pfRe5rcZBhYznHZCUV7M");
mintNFT의 인자는 이전에 저희가 만든 metadata의 ipfs 링크입니다.
