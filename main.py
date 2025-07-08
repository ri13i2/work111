from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
import asyncio
import datetime

BOT_TOKEN = "7799209368:AAF_gN870y-iXBMGvT1QUj0PGdNNQKZS-m0"
TARGET_CHAT_ID = "@heaven111122"

keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton("📛 공지 글 읽으러 가기 (필독) 📛", url="https://t.me/ac777115")],
    [InlineKeyboardButton("💎 일자리 전용 사이트 💎", url="https://t.me/ac777115")],
    [
        InlineKeyboardButton("↗ 소통방", url="https://t.me/heaven111122"),
        InlineKeyboardButton("↗ 공지채널", url="https://t.me/ac777115")
    ],
    [InlineKeyboardButton("↗ 스포츠픽방 및 협력업체", url="https://t.me/kuinkujik")],
    [InlineKeyboardButton("📩 문의 및 신고", url="https://t.me/rsdn114")]
])

image_path = "taegukgi.jpg"
text = "일자리천국 안내 패널입니다.\n아래 버튼을 통해 필요한 채널에 참여하세요."

async def send_message():
    bot = Bot(token=BOT_TOKEN)
    print("✅ 봇이 정상 실행 중입니다. 30분마다 메시지를 보냅니다.")

    while True:
        try:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"📤 [{now}] 메시지 전송 시도...")

            with open(image_path, 'rb') as img:
                await bot.send_photo(
                    chat_id=TARGET_CHAT_ID,
                    photo=img,
                    caption=text,
                    reply_markup=keyboard
                )

            print(f"✅ [{now}] 메시지 전송 완료.")
        except Exception as e:
            print(f"❌ 에러 발생: {e}")

        print("⏱️ 대기 중... 다음 전송까지 30분 남음.\n")
        await asyncio.sleep(1800)

async def main():
    await send_message()

if __name__ == "__main__":
    asyncio.run(main())
